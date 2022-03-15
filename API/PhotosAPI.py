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

CLIENT_SECRET_FILE = "C:/Users/liamm/Desktop/MyTile/API/credentials.json"


class PhotosAPI():
    def __init__(self):
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

        while(first_album.get("title") != "MyTile Album"):
            first_album = next(album_iterator)

        self.album_id = first_album.get("id")

    def getURLs(self):
        media_manager = Media(self.service)

        album_media_list = list(media_manager.search_album(self.album_id))

        self.base_urls = []

        for media in album_media_list:
            self.base_urls.append(media.get("baseUrl"))

    def createImages(self):
        self.photos = []

        for url in self.base_urls:
            image_url = "{}=w275-h300".format(url)
            image_bytes = urlopen(image_url).read()
            #img = PILImage.open(io.BytesIO(image_bytes))
            self.photos.append(PILImage.open(io.BytesIO(image_bytes)))
            #self.photos.append(ImageTk.PhotoImage(img))
    
    def getPhotos(self):
        return self.photos
            
            


# root = Tk()

# canvas = Canvas(root, width=600, height=400, bg="white")
# #512 341
# canvas.pack(side="top", fill="both", expand="yes")

# image_url = "{}=w512-h341".format(base_url)

# image_bytes = urlopen(image_url).read()

# img = PILImage.open(io.BytesIO(image_bytes))

# photo = ImageTk.PhotoImage(img)
# canvas.create_image(10,10, image=photo, anchor="nw")

# root.mainloop()

api = PhotosAPI()