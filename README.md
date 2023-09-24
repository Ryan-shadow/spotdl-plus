# Spotdl-Plus
 
## Spotifly To Folder




### Create a Spotifly developer account & Other settings


* Go to https://developer.spotify.com/ , than create a spotifly developer account
* Go to spotifly developer dashboard (https://developer.spotify.com/dashboard) 
* Create a app , ```Redirect URI``` can be ```http://localhost:8080/callback```

![image](https://github.com/Ryan-shadow/spotdl-plus/assets/121378653/bc6e3f64-7d59-4a3d-9d17-4bfa63bf8752)
* Go to your app home page , click settings


![image](https://github.com/Ryan-shadow/spotdl-plus/assets/121378653/da84b464-b28e-452e-afd6-44cd6366b0e2)
* Copy ```Client ID``` and ```Client secret``` to ```config.json```
* Change ```SaveDircetory``` to where you want to save all of downloaded playlists (use ```/``` not ```\``` !!!)

### VVV__ If you're useing python __VVV
### ONLY WORKS ON PYTHON 3.9.0 ! 
### [https://www.python.org/downloads/release/python-390/](https://www.python.org/downloads/release/python-390/#:~:text=Full%20Changelog-,Files,-Version)
```
pip install spotipy
pip install spotdl
```
