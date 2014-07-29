from youtube import get_list_of_playlists,get_videos_from_playlist
from downloader import mp3_encode,download_video
from tags import add_all_tags
import spotify
import logging
import os
import utils
import tags
import sys
def setup_logging():
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                      datefmt='%m-%d %H:%M',
                      filename='music-yt.log',
                      filemode='w')
  console = logging.StreamHandler()
  console.setLevel(logging.INFO)
  formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
  console.setFormatter(formatter)
  logging.getLogger('').addHandler(console)

if __name__ == '__main__':
  setup_logging()
  for playlist_id,playlist_name in get_list_of_playlists():
    if playlist_name.startswith("Music"):
      for video in get_videos_from_playlist(playlist_id):
        if video in utils.downloaded_videos:
          logging.info("Already downloaded video : " + video + ". Skipping.")
          continue
        try:
          m4a_file = download_video(video)
          if m4a_file is None or len(m4a_file) == 0:
            logging.error("Skipping : " + video + " because it was not downloaded")
            continue
        except Exception, e:
          logging.error("Could not download video : " + video)
          logging.error(e)
          continue
        mp3_file = mp3_encode(m4a_file)
        tags.set_video_name(mp3_file, video)
        os.remove(m4a_file)
        add_all_tags(mp3_file)

