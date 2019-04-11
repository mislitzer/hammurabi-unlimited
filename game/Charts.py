import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk
import urllib
import json
import pandas as pd
import numpy as np



LARGE_FONT=("Verdana",12)
style.use("ggplot")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)

class SeaofBTCapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand="True")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf(stringtoprint):
    print(stringtoprint)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="StartPage")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit page1",
                            command=lambda: qf("yoyo"))
        button1.pack()

app=SeaofBTCapp()
app.mainloop()



def animate(i):
    pullData = open("sampleData.txt","r").read()
    dataList =pullData.split('\n')
    xList=[]
    yList=[]
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList)

class Page(tk.Frame):
    def __init__(selfself, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page")
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self,text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        canvas =FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

#root=Tk()
#root.mainloop()
# app= SeaofBTCapp()
# ani = animation.FuncAnimate(f, animate, interval=1000)
