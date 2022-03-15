import tkinter as tk
from tkinter import *
from Tiles import *
import threading
import time

class GUI():
    def __init__(self):
        self.width = 1200
        self.height = 800

        self.rows = 2
        self.columns = 3


        self.window = tk.Tk()
        
        weather = WeatherTile(self.window, self.width, self.height, 0, 0, 2, 3)

        #spotify = SpotifyTile(self.window, self.width, self.height, 0, 1, 2, 3)
        threading.Thread(target=self.spotify_thread).start()
        
        threading.Thread(target=self.photo_thread).start()
        #photo = PhotoTile(self.window, self.width, self.height, 0, 2, 2, 3)

        self.baseTile4 = self.makeFrame("purple")
        self.baseTile4.pack_propagate(False)
        self.baseTile4.grid(row = 1, column = 0, sticky= "nsew")
        self.addLabel(self.baseTile4, "Red")

        self.baseTile5 = self.makeFrame("red")
        self.baseTile5.pack_propagate(False)
        self.baseTile5.grid(row = 1, column = 1, sticky= "nsew")
        self.addLabel(self.baseTile5, "Red")

        self.baseTile6 = self.makeFrame("blue")
        self.baseTile6.pack_propagate(False)
        self.baseTile6.grid(row = 1, column = 2, sticky= "nsew")
        self.addLabel(self.baseTile6, "Red")

        self.window.geometry(str(self.width) + "x" + str(self.height))

        self.window.mainloop()
    
    def photo_thread(self):
        photo = PhotoTile(self.window, self.width, self.height, 0, 2, 2, 3)
    
    def spotify_thread(self):
        spotify = SpotifyTile(self.window, self.width, self.height, 0, 1, 2, 3)

    def makeFrame(self, color):
        
        frame = tk.Frame(self.window, width= self.width / self.columns, height= self.height / self.rows, background=color)

        #label = tk.Label(master = frame, text=color)
        #label.pack()
        
        return frame
    
    def addLabel(self, frame, title):
        label = tk.Label(master = frame, text=title)
        label.pack()

gui = GUI()

