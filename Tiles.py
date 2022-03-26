import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from API.PhotosAPI import PhotosAPI
from API.SpotifyAPI.SpotifyAPI import SpotifyAPI
import threading
import time
import datetime
from urllib.request import urlopen
import PIL.Image as PILImage
import base64
import urllib
import io
import threading

class Tile():
    def __init__(self, window, width, height, row, column, rows, columns):
        self.title = "Tile"
        self.window = window
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.rows = rows
        self.columns = columns
        self.color = "gray"
        self.forColor = "white"
        self.setup()
    
    def setup(self):
        self.frame = self.makeFrame()
        self.addLabel(self.frame, self.title)

    def makeFrame(self):
        
        frame = tk.Frame(self.window, width= self.width / self.columns, height= self.height / self.rows, background= self.color)
        frame.pack_propagate(False)
        frame.grid(row = self.row, column = self.column, sticky = "nsew")
                
        return frame
    
    def addLabel(self, frame, title):
        label = tk.Label(master=frame, text=title, bg=self.color, fg=self.forColor)
        label.pack(padx=6, pady=10)

class WeatherTile(Tile):
    
    def __init__(self, window, width, height, row, column, rows, columns):
        self.window = window
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.rows = rows
        self.columns = columns
        self.title = "Weather"
        self.color = "blue"
        self.forColor = "black"
        self.setup()

        

class SpotifyTile(Tile):
    
    def __init__(self, window, width, height, row, column, rows, columns):
        self.title = "Spotify"
        self.color = "black"
        self.forColor = "green"
        self.songLabel = tk.StringVar()
        self.songLabel.set("")
        self.artistLabel = tk.StringVar()
        self.artistLabel.set("")
        self.window = window
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.rows = rows
        self.columns = columns
        self.currentSong = ""
        self.currentArtist = ""
        self.imageLink = ""
        self.finished_image = None
        self.api = SpotifyAPI()
        self.updateAPIInfo()
        self.setup()
        self.addPhoto()
        self.loop()
        # threading.Thread(target=self.loop()).start()
        # threading.Thread(target=self.updateProgBar()).start()
        
    
    def addPhoto(self):
        self.songLabel.set(self.currentSong)
        self.artistLabel.set(self.currentArtist)
        img = Image.open("image.png")
        resized_image= img.resize((250, 250))
        new_image= ImageTk.PhotoImage(resized_image)
        self.finished_image = new_image
        self.coverArt = Label(self.frame, image=new_image)
        self.coverArt.image = new_image
        self.coverArt.pack()
        Label(self.frame, textvariable=self.songLabel, bg=self.color, fg=self.forColor).pack(pady=4)
        Label(self.frame, textvariable=self.artistLabel, bg=self.color, fg=self.forColor).pack()
        # self.progBar = ttk.Progressbar(
        #     self.frame,
        #     orient="horizontal",
        #     mode="determinate",
        #     length = 200
        # )
        # self.progBar.pack()
    
    def updateAPIInfo(self):
        self.currentSong, self.currentArtist, self.imageLink = self.api.getCurrentSongData()

    def updateImage(self):
        if(self.imageLink != "None"):
            raw_data = urllib.request.urlopen(self.imageLink).read()
            im = Image.open(io.BytesIO(raw_data))
            im = im.resize((250, 250))
            self.finished_image = ImageTk.PhotoImage(im)

    def updateProgBar(self):
        while(1 == 1):
            time.sleep(1)
            self.progBar['value'] += 1

    def loop(self):
        time.sleep(0)
        while(1 == 1):
            time.sleep(5)
            self.updateAPIInfo()
            self.updateImage()
            self.songLabel.set(self.currentSong)
            self.artistLabel.set(self.currentArtist)
            self.coverArt.configure(image=self.finished_image)
            self.coverArt.image = self.finished_image
            

class PhotoTile(Tile):
    
    def __init__(self, window, width, height, row, column, rows, columns):
        self.title = "Photos"
        self.color = "white"
        self.forColor = "black"
        self.dateLabel = tk.StringVar()
        self.dateLabel.set("")
        self.window = window
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.rows = rows
        self.columns = columns
        self.startTime = datetime.datetime.now().time()
        self.api = PhotosAPI()
        self.photos = self.api.getPhotos()
        self.setup()
        self.addPhoto()
        self.loop()

        
    def addPhoto(self):
        new_image = ImageTk.PhotoImage(self.photos[0])
        self.dateLabel.set(self.api.getDates()[0])
        self.l1 = Label(self.frame, image=new_image)
        self.l1.image = new_image
        self.l1.pack()
        Label(self.frame, textvariable=self.dateLabel, bg=self.color, fg=self.forColor).pack()

    #def elapsedTime(self):
        #if datetime.datetime.now().time() - self.startTime >= 
    
    def loop(self):
        counter = 1
        dates = self.api.getDates()
        while(1 == 1):
            time.sleep(5)
            new_image = ImageTk.PhotoImage(self.photos[counter])
            self.l1.configure(image=new_image)
            self.l1.image = new_image
            self.dateLabel.set(dates[counter])
            if counter + 1 == len(self.photos):
                counter = 0
            else:
                counter += 1

#print(datetime.datetime.now().time() - self.startTime)

        