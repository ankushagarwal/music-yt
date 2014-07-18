import subprocess

youtube_url = "https://www.youtube.com/watch?v="

def download_video(video_id):
  url = youtube_url + video_id
  p = subprocess.Popen(["youtube-dl", "-f", "bestaudio", "-o", "/tmp/%(title)s.%(ext)s", url], stdout=subprocess.PIPE)
  result = p.communicate()[0]

  if p.returncode == 0:
    for line in result.split("\n"):
      if line.startswith('[download] Destination:'):
        return line.split('[download] Destination:')[1].strip()
      if line.endswith('has already been downloaded'):
        return line.split('[download]')[1].split('has already been downloaded')[0].strip()

def mp3_encode(m4a_file):
  mp4_file = m4a_file.replace(".m4a", ".mp3")
  p = subprocess.call(["ffmpeg", "-i", m4a_file, mp4_file])
  return mp4_file


if __name__ == '__main__':
  print "Filename = " + mp3_encode(download_video("SiUkZhz06aA"))

