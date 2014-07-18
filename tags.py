from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from mutagen.easyid3 import EasyID3

import tempfile
import requests
import spotify
def download_album_art(album_art_url):
  f = tempfile.NamedTemporaryFile(delete=False)
  r = requests.get(album_art_url)
  for chunk in r.iter_content(16384):
    f.write(chunk)
  f.close()
  return f.name

def add_album_art(file_name, album_art_url):
  audio = MP3(file_name, ID3=ID3)

  # add ID3 tag if it doesn't exist
  try:
      audio.add_tags()
  except error:
      pass
  album_art_file = download_album_art(album_art_url)
  audio.tags.add(
      APIC(
          encoding=3, # 3 is for utf-8
          mime='image/jpeg', # image/jpeg or image/png
          type=3, # 3 is for the cover image
          desc=u'Cover',
          data=open(album_art_file).read()
      )
  )
  audio.save()

def add_all_tags(mp3_file):
  track_name = mp3_file.split('/')[-1]
  track_name = track_name.replace('.mp3', '')
  result = spotify.get_track_meta_data(track_name)
  album_data = spotify.get_album(result['album']['id'])
  audio = EasyID3(mp3_file)
  audio["title"] = result['name']
  audio["album"] = result['album']['name']
  audio["artist"] = album_data['artists'][0]['name']
  #audio["year"] = album_data["release_date"].split("-")[0]
  audio.save()
  add_album_art(mp3_file, album_data['images'][0]['url'])

if __name__ == '__main__':
  add_all_tags('/tmp/Pitbull - International Love.mp3')
  #add_album_art('/tmp/Pitbull - International Love ft. Chris Brown.mp3', 'https://i.scdn.co/image/d962669f8cb25b4d41b5f8970960d819ea88e2fc')
