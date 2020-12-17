# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 19:17:25 2020

@author: sujit
"""

from pytube import YouTube

from tkinter import *

root = Tk()


root.geometry("300x400")
root.title("youtube video downloader")

def youtube():
    a = var.get() #https://www.youtube.com/watch?v=0NV1KdWRHck
    ytvideo = YouTube(a).streams.filter(progressive = True, file_extension="mp4").order_by('resolution').desc().first()
    ytvideo.download(r"C:\Users\sujit\tedtalk")    
    print("entrybox",a)


l1 = Label(root, text = "YouTube video ",fg="red",font =('bold',20))
l1.place(x=70,y=20)

var = StringVar()
e1 = Entry(root,textvariable=var,width=60)
e1.place(x=40,y=80)

b1 = Button(root,text ="download" ,bg = "green", fg = "white",width=20 ,command=youtube)
b1.place(x=70,y=120)













root.mainloop()