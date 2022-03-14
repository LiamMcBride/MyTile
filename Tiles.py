import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

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
        self.title = "Weather"
        self.window = window
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.rows = rows
        self.columns = columns
        self.color = "blue"
        self.forColor = "black"
        self.setup()

class SpotifyTile(Tile):
    
    def __init__(self, window, width, height, row, column, rows, columns):
        self.title = "Spotify"
        self.window = window
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.rows = rows
        self.columns = columns
        self.color = "black"
        self.forColor = "green"
        self.setup()
        self.addPhoto()
    
    def addPhoto(self):
        img = Image.open("image.png")
        resized_image= img.resize((250, 250))
        new_image= ImageTk.PhotoImage(resized_image)
        Label(self.frame, image=new_image).pack()
        Label(self.frame, text="Happier - Marshmellow", bg=self.color, fg=self.forColor).pack()
        