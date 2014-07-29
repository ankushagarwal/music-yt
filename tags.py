from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from mutagen.easyid3 import EasyID3

import logging
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
  logging.info("Adding tags to " + mp3_file)
  track_name = mp3_file.split('/')[-1]
  track_name = track_name.replace('.mp3', '')
  result = spotify.get_track_meta_data(track_name)
  if result is None:
    logging.error("Could not find tags for track : " + track_name)
    return
  album_data = spotify.get_album(result['album']['id'])
  audio = EasyID3(mp3_file)
  audio["title"] = result['name']
  logging.debug("Title Tag = " + str(audio["title"]))
  audio["album"] = result['album']['name']
  logging.debug("Album Tag = " + str(audio['album']))
  audio["artist"] = album_data['artists'][0]['name']
  logging.debug("Artist Tag = " + str(audio['artist']))
  #audio["year"] = album_data["release_date"].split("-")[0]
  audio.save()
  try:
    add_album_art(mp3_file, album_data['images'][0]['url'])
  except Exception, e:
    logging.error("Could not add album art for " + track_name)


if __name__ == '__main__':
  add_all_tags('/tmp/Pitbull - International Love.mp3')
  #add_album_art('/tmp/Pitbull - International Love ft. Chris Brown.mp3', 'https://i.scdn.co/image/d962669f8cb25b4d41b5f8970960d819ea88e2fc')
