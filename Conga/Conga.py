#coding: utf-8

import cv2
import numpy as np
#from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk
import tkinter.ttk as ttk

import ex
import bb
import ZD
import agg

def openC(path):
    path.text = fd.askopenfilename()
    path.delete(1.0,tk.END)
    path.insert(1.0,path.text)
    print(path.text)
    #img = tk.PhotoImage(file = pathIN.text)

    #cnv.create_image(0,0,image = img,anchor = tk.NW)
    #lav.config(image=img)
        
def convEX(infile,infolder,outname,P,outfolder,AGG):
    print("ex")
    if(AGG):
        poi = float(P)
        c = ex.ex(infile,outname,P,outfolder)
        del(c)
    else:
        c = agg.flower(infolder,outfolder,outname,0,P)
        del(c)
def convBB():
    print("bb")
def convZD():
    print("ZD")
def setup():
    win = tk.Tk("conga","conga","conga")
    win.geometry("970x600")

    lpathIN = tk.Label(win,text = "入力パス")
    lpathIN.grid(column = 0,row = 1)

    pathIN = tk.Text(win,width = 50,height = 1)
    pathIN.grid(column = 0,row = 2)

    bPathIn = tk.Button(win,text = "hiraku")
    bPathIn.grid(column = 1,row = 2,sticky = "W")
    bPathIn.bind("<1>",lambda a:openC(pathIN))
    #pathIN.place(x = 0,y = 20,width = 240,height = 20)
    #texts.pack()
    #texts.columnconfigure(0,weight = 1)
    #texts.rowconfigure(0,weight = 1)


    #cnv = tk.Canvas(win,width = 300,height = 300)
    #cnv.place(x = 0,y = 60)

    #lav = tk.Label(win,width = 300,height = 300)
    #lav.place(x=301,y=60)

    #img = tk.PhotoImage(file = "e:/ttv2.png")

    #cnv.create_image(0,0,image = img,anchor = tk.NW)
    #lav.config(image=img)

    lpathOUT = tk.Label(win,text = "出力名")
    lpathOUT.grid(column = 0,row = 4)

    pathOUT = tk.Text(win,width = 50,height = 1)
    pathOUT.grid(column = 0,row = 5)

    bPathOUT = tk.Button(win,text = "hiraku")
    bPathOUT.grid(column = 1,row = 5,sticky = "W")
    bPathOUT.bind("<1>",lambda b:openC(pathOUT))

    lINfolder = tk.Label(win,text = "入力フォルダパス")
    lINfolder.grid(column = 0,row = 7)

    INfolder = tk.Text(win,width = 50,height = 1)
    INfolder.grid(column = 0,row = 8)

    bINfolder = tk.Button(win,text = "hiraku")
    bINfolder.grid(column = 1,row = 8,sticky = "W")
    bINfolder.bind("<1>",lambda c:openC(INfolder))

    lOUTfolder = tk.Label(win,text = "出力フォルダパス")
    lOUTfolder.grid(column = 0,row = 10)

    OUTfolder = tk.Text(win,width = 50,height = 1)
    OUTfolder.grid(column = 0,row = 11)

    bOUTfolder = tk.Button(win,text = "hiraku")
    bOUTfolder.grid(column = 1,row = 11,sticky = "W")
    bOUTfolder.bind("<1>",lambda d:openC(OUTfolder))

    lAlphafile = tk.Label(win,text = "アルファ画像パス")
    lAlphafile.grid(column = 0,row = 13)

    Alphafile = tk.Text(win,width = 50,height = 1)
    Alphafile.grid(column = 0,row = 14)

    bAlphafile = tk.Button(win,text = "hiraku")
    bAlphafile.grid(column = 1,row = 14,sticky = "W")
    bAlphafile.bind("<1>",lambda e:openC(Alphafile))

    lP = tk.Label(win,text = "強度")
    lP.grid(column = 0,row = 16,sticky = "W")

    P = tk.Text(win,width = 5,height = 1)
    P.grid(column = 0,row = 17,sticky = "W")

    val = tk.BooleanVar()
    val.set(False)
    Agg = tk.Checkbutton(win,text = "連続")
    Agg.grid(column = 3,row = 17,sticky = "W")

    bEdge = tk.Button(win,text = "エッジ")
    bEdge.grid(column = 0,row = 17,sticky = "E")
    bEdge.bind("<1>",lambda e:convEX(pathIN.get("1.0","end"),INfolder.get("1.0","end"),pathOUT.get("1.0","end"),P.get("1.0","end"),OUTfolder.get("1.0","end"),val.get()))

    bAlpha = tk.Button(win,text = "アルファ")
    bAlpha.grid(column = 1,row = 17,sticky = "W")
    #bAlpha.bind("<1>",lambda e:convBB())

    bNoise = tk.Button(win,text = "ノイズ")
    bNoise.grid(column = 2,row = 17,sticky = "W")
    #bNoise.bind("<1>",lambda e:openC(Alphafile))

    

    win.mainloop()
    
if __name__ == "__main__":
    setup()