import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from API.PhotosAPI import PhotosAPI
from API.SpotifyAPI.SpotifyAPI import SpotifyAPI
from API.WeatherAPI.WeatherAPI import WeatherAPI
import threading
import time
import datetime
from urllib.request import urlopen
import PIL.Image as PILImage
import base64
import urllib
import io
import threading
import requests
class Tile():
    def __init__(self, window, width, height, row, column, rows, columns):
        self.title = "Tile"
        self.fontSize = 18
        self.fontType = "arial"
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
        label = tk.Label(master=frame, text=title, font=(self.fontType, 25), bg=self.color, fg=self.forColor)
        label.pack(padx=6, pady=10)

class WeatherTile(Tile):
    #I want to dynamically change the background color to reflect time of day/weather
    def __init__(self, window, width, height, row, column, rows, columns):
        self.fontSize = 18
        self.fontType = "arial"
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
        self.highLabel = tk.StringVar()
        self.lowLabel = tk.StringVar()
        self.hourlyTemps = [None, None, None, None, None, None] #holds siz string var
        self.currentLabel = tk.StringVar()
        self.api = WeatherAPI()
        self.weatherData = self.api.getWeatherData()
        self.setup()
        self.setupLayout()

    def setupLayout(self):
        self.currentLabel.set(self.getCurrentTemp())
        self.highLabel.set("High: " + self.getHigh())
        self.lowLabel.set("Low: " + self.getLow())
        

        for i in range(0,6):
            self.setHourlyTemp(i)
        new_image = self.getImage()

        self.l1 = Label(self.frame, image=new_image)
        self.l1.image = new_image
        self.l1.pack(side="left")
        
        Label(self.frame, textvariable=self.currentLabel, font=(self.fontType, 35), bg=self.color, fg=self.forColor).pack()
        Label(self.frame, textvariable=self.highLabel, font=(self.fontType, self.fontSize), bg=self.color, fg=self.forColor).pack(pady=4)
        Label(self.frame, textvariable=self.lowLabel, font=(self.fontType, self.fontSize), bg=self.color, fg=self.forColor).pack()
        

        for i in range(0, 6):
            Label(self.frame, textvariable=self.hourlyTemps[i], font=(self.fontType, self.fontSize), bg=self.color, fg=self.forColor).pack()

        print(self.getHourData(1))

    def getHigh(self):
        return str(round(self.weatherData["forecast"]["forecastday"][0]["day"]["maxtemp_f"])) + " °F"

    def getLow(self):
        return str(round(self.weatherData["forecast"]["forecastday"][0]["day"]["mintemp_f"])) + " °F"

    def getCurrentTemp(self):
        return str(round(self.weatherData["current"]["temp_f"])) + " °F"

    def getHourData(self, offsetFromCurrentHour):
        #currentTime = datetime.datetime().today().hour
        return self.weatherData["forecast"]["forecastday"][0]["hour"][(12) + offsetFromCurrentHour]

    def getImage(self):
        imageLink = "http:" + self.weatherData["current"]["condition"]["icon"]

        # raw_data = urllib.request.urlopen(imageLink)
        # image = Image.open(io.BytesIO(raw_data))




        # link = urllib.request(imageLink)
        # raw_data = urllib.urlopen(link)

        raw_data = urllib.request.urlopen(imageLink).read()
        im = Image.open(io.BytesIO(raw_data))
        img_size = int((self.width / self.columns) * .3)
        im = im.resize((img_size, img_size))
        return ImageTk.PhotoImage(im)

    def setHourlyTemp(self, offset):
        offset = offset - 1
        hourlyTemp = self.getHourData(offset + 1)["temp_f"]

        if(self.hourlyTemps[offset] == None):
            self.hourlyTemps[offset] = tk.StringVar()
        
        self.hourlyTemps[offset].set(hourlyTemp)


    

        

class SpotifyTile(Tile):
    
    def __init__(self, window, width, height, row, column, rows, columns):
        self.title = "Spotify"
        self.color = "black"
        self.forColor = "green"
        self.fontSize = 18
        self.fontType = "arial"
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
        img_size = int((self.width / self.columns) * .625)
        resized_image= img.resize((img_size, img_size))
        new_image= ImageTk.PhotoImage(resized_image)
        self.finished_image = new_image
        self.coverArt = Label(self.frame, image=new_image)
        self.coverArt.image = new_image
        self.coverArt.pack()
        Label(self.frame, textvariable=self.songLabel, font=(self.fontType, self.fontSize), bg=self.color, fg=self.forColor).pack(pady=4)
        Label(self.frame, textvariable=self.artistLabel, font=(self.fontType, self.fontSize), bg=self.color, fg=self.forColor).pack()
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
            img_size = int((self.width / self.columns) * .625)
            im = im.resize((img_size, img_size))
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
        self.fontSize = 18
        self.fontType = "arial"
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
        Label(self.frame, textvariable=self.dateLabel, font=(self.fontType, self.fontSize), bg=self.color, fg=self.forColor).pack()

    #def elapsedTime(self):
        #if datetime.datetime.now().time() - self.startTime >= 
    
    def loop(self):
        counter = 1
        dates = self.api.getDates()
        while(1 == 1):
            time.sleep(5)
            img_size = int((self.width / self.columns) * .625)
            ratio = img_size / self.photos[counter].size[0]
            im = self.photos[counter].resize((img_size, int(self.photos[counter].size[1] * ratio)))
            new_image = ImageTk.PhotoImage(im)
            self.l1.configure(image=new_image)
            self.l1.image = new_image
            self.dateLabel.set(dates[counter])
            if counter + 1 == len(self.photos):
                counter = 0
            else:
                counter += 1

#print(datetime.datetime.now().time() - self.startTime)

        