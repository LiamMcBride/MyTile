import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from API.PhotosAPI import PhotosAPI
import threading
import time
import datetime

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
        label.pack()

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
        self.window = window
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.rows = rows
        self.columns = columns
        self.setup()
        self.addPhoto()
        self.loop()
    
    def addPhoto(self):
        img = Image.open("image.png")
        resized_image= img.resize((250, 250))
        new_image= ImageTk.PhotoImage(resized_image)
        Label(self.frame, image=new_image).pack()
        self.l1 = Label(self.frame, text="Happier - Marshmellow", bg=self.color, fg=self.forColor).pack()

    def loop(self):
        
        while(1 == 1):
            time.sleep(2)
            self.l1.text = "Hi"
            time.sleep(2)
            self.l1.text = "bye"

class PhotoTile(Tile):
    
    def __init__(self, window, width, height, row, column, rows, columns):
        self.title = "Photos"
        self.color = "white"
        self.forColor = "black"
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
        self.l1 = Label(self.frame, image=new_image)
        self.l1.image = new_image
        self.l1.pack()
        Label(self.frame, text="Happier - Marshmellow", bg=self.color, fg=self.forColor).pack()

    #def elapsedTime(self):
        #if datetime.datetime.now().time() - self.startTime >= 
    
    def loop(self):
        counter = 1
        while(1 == 1):
            time.sleep(5)
            new_image = ImageTk.PhotoImage(self.photos[counter])
            self.l1.configure(image=new_image)
            self.l1.image = new_image
            if counter + 1 == len(self.photos):
                counter = 0
            else:
                counter += 1

#print(datetime.datetime.now().time() - self.startTime)

        