import re
import secret
import json
import spotipy
import logging

def filter_keywords_from_title(title):
    keywords = [  r"(\(\s*official video\s*\))",
                  r"(\[\s*official video\s*\])",
                  r"(official video)",
                  r"(officialvideo)",
                  r"(\[\s*lyrics\s*\])",
                  r"(\[\s*lyric\s*\])",
                  r"(lyrics)",
                  r"(lyric)",
                  r"(\(\s*\))",
                  r"(\[\s*\])",
                  r"(.official video.)",
                  r"(\(\s*official music video\s*\))",
                  r"(\[\s*official music video\s*\])",
                  r"(\(\s*lyric video\s*\))",
                  r"(\[\s*lyrics video\s*\])",
                  r"(\(\s*explicit\s*\))",
                  r"(\[\s*explicit\s*\])",
                  r"(\(\s*official\s*\))",
                  r"(\[\s*official\s*\])",
                  r"(\(\s*audio\s*\))",
                  r"(\[\s*audio\s*\])",
                  r"(\(.*\))",
                  r"(\[.*\])",
                  r"(-)",
                    ]
    p = re.compile('|'.join(keywords), re.IGNORECASE)
    while p.subn(' ', title)[1] > 0:
      title = p.subn(' ', title)[0].strip()
    return title

def remove_ft(title):
  threshold = (len(title))*0.25
  index = title.lower().find("ft")
  if index <= threshold:
    return title
  else:
    return title[:index]

def get_track_meta_data(track_name):
  original_track_name = track_name
  logging.info("Fetching track metadata for track : " + track_name)
  track_name = filter_keywords_from_title(track_name)
  sp = spotipy.Spotify()
  try:
    search_result = sp.search(track_name, limit = 1)['tracks']['items'][0]
    return search_result
  except Exception, e:
    track_without_ft = remove_ft(track_name)
    logging.info("Failed to get any results with : " + track_name + " Retrying with "
                  + track_without_ft)
    try:
      search_result = sp.search(track_without_ft, limit = 1)['tracks']['items'][0]
      return search_result
    except Exception, e:
      logging.info("Still nothing for " + track_without_ft)
      return None

def get_album(album_id):
  sp = spotipy.Spotify()
  return sp.album(album_id)

if __name__ == '__main__':
  print filter_keywords_from_title("David Guetta - She Wolf (Falling To Pieces) ft. Sia (Official Video)")
