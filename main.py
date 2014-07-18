from youtube import get_list_of_playlists,get_videos_from_playlist
from downloader import mp3_encode,download_video
from tags import add_all_tags
import spotify

if __name__ == '__main__':
  for playlist_id,playlist_name in get_list_of_playlists():
    if playlist_name.startswith("Music"):
      for video in get_videos_from_playlist(playlist_id):
        print "Downloading video : " + video
        mp3_file = mp3_encode(download_video(video))
        print "Tagging file : " + mp3_file
        add_all_tags(mp3_file)

