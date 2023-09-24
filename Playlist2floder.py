import subprocess
import re
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
DownloadHomePath = r"E:\Users\Ryan\Music\Spotifly" #YOUR HOME DIRCETORY

#spotipy config
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your client_id',
                                               client_secret='your client_secret',
                                               redirect_uri='http://localhost:8080/callback',
                                               scope='user-library-read'))
playlist_url = input("Enter the Spotify playlist URL: ")
# Spotify playlist url
playlist_id = re.search(r'playlist/([\w]+)',playlist_url ).group(1)

folder_name = sp.playlist(playlist_id)['name']
print(f"Playlist Name: {folder_name}")

# check is folder was exists
folder_path = str(os.path.join(DownloadHomePath, folder_name))

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"folder '{folder_name}' successfully created in '{DownloadHomePath}'")
else:
    print(f"folder '{folder_name}' already exists in '{DownloadHomePath}'")
print(f"ready to download to {folder_path} ")
try:
    print(f"ready to run: spotdl {playlist_url} --output {folder_path}")
    subprocess.run(["spotdl", playlist_url, "--output", folder_path])

    print("Download successful.")
except subprocess.CalledProcessError as e:
    print("Download failed:", e)
