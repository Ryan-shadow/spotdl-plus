import subprocess
import re
import os
import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
#pyinstaller Spotifly_To_Folder.py --onefile --name Spotdl-plus --icon=spotifly_cmd.ico -w
print("|          Welcom :)                                             |")
print("|    By Lin Zit Ting On Github https://github.com/Ryan-shadow    |")
print("|________________________________________________________________|")
print("")

API_KEY = "AIzaSyDWXRfl_-rUHjHLm0KWjLhaB9pN7S5lA9I"
youtube = build('youtube', 'v3', developerKey=API_KEY)
# get config file path
config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

# open json config file
with open(config_file_path, 'r') as json_file:
    ConfigData = json.load(json_file)

DownloadHomePath = ConfigData["SaveDircetory"] #YOUR HOME DIRCETORY

#spotipy config
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ConfigData["client_id"],
                                               client_secret=ConfigData["client_secret"],
                                               redirect_uri=ConfigData["redirect_uri"],
                                               scope='user-library-read'))
object_url = input("Enter the Spotify or YT Music  Playlist , Album or Track URL: ")
# Spotify playlist url
url_type = ""

try:
    object_id = re.search(r'playlist/([\w]+)', object_url)
    if object_id:
        object_id = object_id.group(1)
        url_type = "playlist"
    else:
        raise AttributeError("Object ID not found")  # 引發 AttributeError    
except AttributeError as e:
    try:
        object_id = re.search(r'album/([\w]+)', object_url)
        if object_id:
            object_id = object_id.group(1)
            url_type = "album"
        else:
            raise AttributeError("Object ID not found")  # 引發 AttributeError
    except AttributeError as e:
        try:
            object_id = re.search(r'track/([\w]+)', object_url)
            if object_id:
                object_id = object_id.group(1)
                url_type = "track"
            else:
                raise AttributeError("Object ID not found")  # 引發 AttributeError
        except AttributeError as e:
            if object_url.find("youtube.com") == -1:
                url_type = "UNKNOW_TYPE!"
            else:
                if "playlist?list=" in object_url:
                    object_id = re.search(r'playlist?list=([\w]+)', object_url)
                    if object_id:
                        object_id = object_id.group(1)
                        url_type = "YT_playlist"
                elif "watch?v=" in object_url:
                    object_id = re.search(r'watch\?v=([\w]+)', object_url)
                    if object_id:
                        object_id = object_id.group(1)
                        url_type = "YT_watch"





if url_type == "playlist" :
    folder_name = sp.playlist(object_id)['name']
    print(f"Playlist Name: {folder_name}")
    folder_path = str(os.path.join(DownloadHomePath, folder_name))
elif url_type == "album":
    folder_name = sp.album(object_id)['name']
    print(f"Album Name: {folder_name}")
    folder_path = str(os.path.join(DownloadHomePath, folder_name))
elif url_type == "track":
    folder_name = "tracks"
    print(f"Track")
    ArtistName = sp.track(object_id)['artists'][0]['name']
    folder_path = str(os.path.join(DownloadHomePath, folder_name , ArtistName))
elif url_type == "YT_watch":
    
    response = youtube.videos().list(part='snippet', id=object_id, fields='items(snippet(title))').execute()['items'][0]['snippet']['title']
    print(response)

    folder_name = response
    print(f"TPlaylist Name: {folder_name}")
    ArtistName = sp.track(object_id)['artists'][0]['name']
    folder_path = str(os.path.join(DownloadHomePath, folder_name))
else:
    print(f"A {url_type} ") 
    sys.exit()
print(f"Object id : {object_id}")

# check is folder was exists


if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_name}' successfully created in '{DownloadHomePath}'")
else:
    print(f"Folder '{folder_name}' already exists in '{DownloadHomePath}'")
print(f"Ready to download to {folder_path} ")


if(url_type == "youtube"):
    try:
        print(f"Ready to run: yt-dip  {object_url} --audio-format mp3 --concurrent-fragments 2 --no-overwrites --write-thumbnail   --output {folder_path}")
        subprocess.run(["spotdl", object_url,"--audio-format mp3","--concurrent-fragments 2", "--output", folder_path])
        print("Download successful.")
    except subprocess.CalledProcessError as e:
        print("Download failed:", e)

else:
    try:
        print(f"Ready to run: spotdl {object_url} --output {folder_path}")
        subprocess.run(["spotdl", object_url, "--output", folder_path])
        print("Download successful.")
    except subprocess.CalledProcessError as e:
        print("Download failed:", e)

#pyinstaller --onefile --icon=spotifly_cmd.ico Spotifly_To_Folder.py
