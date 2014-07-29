import subprocess
import logging
import sys
from os.path import expanduser
import os

home = expanduser("~")
music_directory = home + "/Music/Youtube"

if not os.path.exists(music_directory):
    os.makedirs(music_directory)

youtube_url = "https://www.youtube.com/watch?v="

def download_video(video_id):
  logging.info("Downloading video : " + video_id)
  url = youtube_url + video_id
  p = subprocess.Popen(["youtube-dl", "-f", "bestaudio", "-o", music_directory + "/%(title)s.%(ext)s", url], stdout=subprocess.PIPE)
  result = p.communicate()[0]
  if p.returncode == 0:
    for line in result.split("\n"):
      if line.startswith('[download] Destination:'):
        return line.split('[download] Destination:')[1].strip()
      if line.endswith('has already been downloaded'):
        return line.split('[download]')[1].split('has already been downloaded')[0].strip()

def mp3_encode(m4a_file):
  mp3_file = m4a_file.replace(".m4a", ".mp3")
  logging.info("mp3 encoding : " + m4a_file)
  p = subprocess.call(["ffmpeg", "-y", "-i", m4a_file, mp3_file], stderr=subprocess.PIPE)
  return mp3_file


if __name__ == '__main__':
  print "Filename = " + mp3_encode(download_video("CdXesX6mYUE"))

