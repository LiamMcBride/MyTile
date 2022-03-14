import tkinter as tk
from tkinter import *

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
        self.setup()
    
    def setup(self):
        self.frame = self.makeFrame()
        self.addLabel(self.frame, self.title)

    def makeFrame(self):
        
        frame = tk.Frame(self.window, width= self.width / self.columns, height= self.height / self.rows, background="blue")
        frame.pack_propagate(False)
        frame.grid(row = self.row, column = self.column, sticky = "nsew")
                
        return frame
    
    def addLabel(self, frame, title):
        label = tk.Label(master = frame, text=title)
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
        self.setup()