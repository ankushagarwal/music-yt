import json
import requests
import sys

try:
  import secret
except Exception, e:
  print "secret.py missing. Please place a secret.py containing the api_key"
  sys.exit(1)


BASE_URL = "https://www.googleapis.com/youtube/v3/"

channel_id="UCJZqoipdcouSv7n-1aW1Zwg"
api_key=secret.api_key

def get_list_of_playlists():
  playlist_list = []
  r = requests.get(BASE_URL + "playlists?" + "part=contentDetails,snippet" + "&channelId=" + channel_id + "&key=" + api_key)
  for playlist in json.loads(r.text)["items"]:
    playlist_list.append([playlist["id"], playlist["snippet"]["title"]])
  return playlist_list

def get_videos_from_playlist(playlist_id):
  videos_list = []
  next_page_token = ""
  last_page = False
  while not last_page:
    r = requests.get(BASE_URL + "playlistItems?" + "part=contentDetails,snippet" + "&playlistId=" + playlist_id + "&key="
                      + api_key + "&maxResults=50" + "&pageToken=" + next_page_token)
    r = json.loads(r.text)
    try:
      next_page_token = r["nextPageToken"]
    except Exception, e:
      last_page = True
    for x in r["items"]:
      videos_list.append(x["contentDetails"]["videoId"])
  return videos_list

  for playlist in json.loads(r.text)["items"]:
    playlist_list.append(playlist["id"])
  return playlist_list


if __name__ == '__main__':
  print get_list_of_playlists()

  for playlist_id,playlist_name in get_list_of_playlists():
    if playlist_name.startswith("Music"):
      print get_videos_from_playlist(playlist_id)
