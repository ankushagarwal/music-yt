from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import tempfile
import requests

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


if __name__ == '__main__':
  add_album_art('/tmp/Pitbull - International Love ft. Chris Brown.mp3', 'https://i.scdn.co/image/d962669f8cb25b4d41b5f8970960d819ea88e2fc')
