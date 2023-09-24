import subprocess
import re
import os
import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

print("|          Welcom :)                                             |")
print("|    By Lin Zit Ting On Github https://github.com/Ryan-shadow    |")
print("|________________________________________________________________|")
print("")

# open json config file
with open('config.json', 'r') as json_file:
    ConfigData = json.load(json_file)

DownloadHomePath = ConfigData["SaveDircetory"] #YOUR HOME DIRCETORY

#spotipy config
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ConfigData["client_id"],
                                               client_secret=ConfigData["client_secret"],
                                               redirect_uri=ConfigData["redirect_uri"],
                                               scope='user-library-read'))
object_url = input("Enter the Spotify Playlist , Album or Track URL: ")
# Spotify playlist url
url_type = ""
try:    
    object_id = re.search(r'playlist/([\w]+)',object_url ).group(1)
    url_type = "playlist"
except AttributeError as e:
    try:
        object_id = re.search(r'album/([\w]+)',object_url ).group(1)
        url_type = "album"
    except AttributeError as e:
        try:
            object_id = re.search(r'track/([\w]+)',object_url ).group(1)
            url_type = "track"
        except AttributeError as e:
            url_type = "UNKNOW_TYPE!"
print(f"A {url_type}")

if url_type == "playlist" :
    folder_name = sp.playlist(object_id)['name']
    print(f"Playlist Name: {folder_name}")

elif url_type == "album":
    folder_name = sp.album(object_id)['name']
    print(f"Album Name: {folder_name}")
elif url_type == "track":
    folder_name = "tracks"
    print(f"Track Name: {folder_name}")
else:
    print(f"A {url_type} , {e}") 
    sys.exit()


# check is folder was exists
folder_path = str(os.path.join(DownloadHomePath, folder_name))

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"folder '{folder_name}' successfully created in '{DownloadHomePath}'")
else:
    print(f"folder '{folder_name}' already exists in '{DownloadHomePath}'")
print(f"Ready to download to {folder_path} ")
try:
    print(f"Ready to run: spotdl {object_url} --output {folder_path}")
    subprocess.run(["spotdl", object_url, "--output", folder_path])

    print("Download successful.")
except subprocess.CalledProcessError as e:
    print("Download failed:", e)
