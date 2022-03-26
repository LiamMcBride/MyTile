import spotipy
from spotipy.oauth2 import SpotifyOAuth
from API.SpotifyAPI.SpotifySecret import CLIENT_ID, CLIENT_SECRET, REDIRECT_LINK
import PIL.Image as PILImage
from PIL import ImageTk
from urllib.request import urlopen
#from SpotifySecret import CLIENT_ID, CLIENT_SECRET, REDIRECT_LINK

#scope = "user-library-read"
# scope = "user-read-currently-playing"

# #sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope), client_credentials_manager=CLIENT_ID)
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT_LINK, scope=scope))

# # results = sp.current_user_saved_tracks()
# # for idx, item in enumerate(results['items']):
# #     track = item['track']
# #     print(idx, track['artists'][0]['name'], " – ", track['name'])

# results = sp.current_user_playing_track()
# artist = results["item"]["artists"][0]['name']
# song = results["item"]['name']
# print(song)

class SpotifyAPI():
    def __init__(self):
        self.authorize()
    
    def authorize(self):
        self.scope = "user-read-currently-playing"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT_LINK, scope=self.scope))

    def createImage(self, url):
        image_url = "{}".format(url)
        image_bytes = urlopen(image_url).read()
        return image_bytes
    
    def getCurrentSongData(self):
        results = self.sp.current_user_playing_track()
        if str(results) == "None":
            return "No Song Playing", "None", "None"
        artist = results["item"]["artists"][0]['name']
        song = results["item"]['name']
        photoArt = results["item"]["album"]["images"][0]

        photoArt = photoArt["url"]

        #print(photoArt)

        return song, artist, (photoArt)

api = SpotifyAPI()

print(api.getCurrentSongData())