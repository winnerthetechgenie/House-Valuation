from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
import os

def change_path():
    path = filedialog.askdirectory() #allows the user to select path from the system
    select_path_label.config(text=path)
   
def download_video():
    #get video link
    video_link = link.get()
    #get storage path
    spath = select_path_label.cget("text")
    screen.title("downloading...")
    #download the video
    mp4_video = YouTube(video_link).streams.get_highest_resolution().download()
    video = VideoFileClip(mp4_video)
    video.close()
    #move file to prefered location
    shutil.move(mp4_video, spath)
  
    screen.title("Download Complete")

screen = Tk()
title = screen.title("YouTube Download")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#add logo
logo_image = PhotoImage(file="youtube.png")

#resize
logo_image = logo_image.subsample(1,1)
canvas.create_image(250, 80, image=logo_image)

#fields
link = Entry(screen, width=50)
link_label = Label(screen, text="Enter video Link: ", font=('arial', 12))
select_path_label = Label(screen, text="Select storage path: ", font=('arial', 12))
select_path_btn = Button(screen, text="Select", width=20, command=change_path)
download_btn = Button(screen, text="Download", command=download_video)

#windows
canvas.create_window(250, 170, window=link)
canvas.create_window(250, 145, window=link_label)
canvas.create_window(250, 300, window=select_path_label)
canvas.create_window(250, 330, window=select_path_btn)
canvas.create_window(250, 370, window=download_btn)




screen.mainloop()