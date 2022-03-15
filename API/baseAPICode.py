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

service = authorize.init(CLIENT_SECRET_FILE)



album_manager = Album(service)

album_iterator = album_manager.list()

first_album = next(album_iterator)
#print(first_album)
first_album_id = first_album.get("id")

media_manager = Media(service)

album_media_list = list(media_manager.search_album(first_album_id))

base_url = album_media_list[0].get("baseUrl")
print(base_url)

root = Tk()

canvas = Canvas(root, width=600, height=400, bg="white")
#512 341
canvas.pack(side="top", fill="both", expand="yes")

image_url = "{}=w512-h341".format(base_url)

image_bytes = urlopen(image_url).read()

img = PILImage.open(io.BytesIO(image_bytes))

photo = ImageTk.PhotoImage(img)
canvas.create_image(10,10, image=photo, anchor="nw")

root.mainloop()