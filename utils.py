import glob
from os.path import expanduser
import os
import tags

home = expanduser("~")
music_directory = home + "/Music/Youtube"
mp3_directory = music_directory + "/mp3"
m4a_directory = music_directory + "/m4a"
if not os.path.exists(mp3_directory):
    os.makedirs(mp3_directory)
if not os.path.exists(m4a_directory):
    os.makedirs(m4a_directory)

mp3_files = glob.glob(mp3_directory + "/*.mp3")
downloaded_videos = []
for f in mp3_files:
  try:
    downloaded_videos.append(tags.get_video_name(f)[0])
  except Exception, e:
    pass