from distutils.filelist import findall
from gphotospy import authorize
from gphotospy.album import *
from gphotospy.media import *
import io
from urllib.request import urlopen
from tkinter import *
from gphotospy.authorize import get_credentials
import PIL.Image as PILImage
from PIL import ImageTk
import datetime

#CLIENT_SECRET_FILE = "C:/Users/liamm/Desktop/MyTile/API/credentials.json"
CLIENT_SECRET_FILE = "C:/Users/liamm/OneDrive/Desktop/MyTile/API/credentials.json"

ALBUM_NAME = "MyTile Album"


class PhotosAPI():
    def __init__(self):
        self.dates = []
        self.start()

    def start(self):
        self.autorize()
        self.findAlbum()
        self.getURLs()
        self.createImages()
       
    
    def autorize(self):
        self.service = authorize.init(CLIENT_SECRET_FILE)
        

    def findAlbum(self):
        album_manager = Album(self.service)

        album_iterator = album_manager.list()
        first_album = next(album_iterator)

        while(first_album.get("title") != ALBUM_NAME):
            first_album = next(album_iterator)

        self.album_id = first_album.get("id")   

    def createDatesArray(self, date):
        dateFormat = "%Y-%m-%dT%H:%M:%SZ"
        correctDate = (datetime.datetime.strptime(date, dateFormat))

        outputFormat = "%d %b, %Y"

        self.dates.append(correctDate.strftime(outputFormat))

    def getURLs(self):
        media_manager = Media(self.service)

        media_iterator = media_manager.list()

        media_id = next(media_iterator).get("id")

        print(media_manager.get(media_id))

        album_media_list = list(media_manager.search_album(self.album_id))

        self.base_urls = []

        for media in album_media_list:
            self.base_urls.append(media.get("baseUrl"))
            date = str(media.get("mediaMetadata").get("creationTime"))
            self.createDatesArray(date)

    def createImages(self):
        self.photos = []

        for url in self.base_urls:
            image_url = "{}=w275-h300".format(url)
            image_bytes = urlopen(image_url).read()
            self.photos.append(PILImage.open(io.BytesIO(image_bytes)))
    
    def getPhotos(self):
        return self.photos

    def getDates(self):
        return self.dates
            

api = PhotosAPI()