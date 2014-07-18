import re
import secret
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
                  r"(\[\s*\])"  ]
    p = re.compile('|'.join(keywords), re.IGNORECASE)
    while p.subn(' ', title)[1] > 0:
      title = p.subn(' ', title)[0].strip()
    return title

if __name__ == '__main__':
  print filter_keywords_from_title("[lyriC][lyrics]Glad you[official video] came() [Official Video]")
