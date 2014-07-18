import re
import secret
import json
import spotipy


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
                  r"(-)",
                    ]
    p = re.compile('|'.join(keywords), re.IGNORECASE)
    while p.subn(' ', title)[1] > 0:
      title = p.subn(' ', title)[0].strip()
    return title

def get_track_meta_data(track_name):
  result = {}
  sp = spotipy.Spotify()
  search_result = sp.search(track_name, limit = 1)['tracks']['items'][0]




if __name__ == '__main__':
  print filter_keywords_from_title("David Guetta - She Wolf (Falling To Pieces) ft. Sia (Official Video)")
