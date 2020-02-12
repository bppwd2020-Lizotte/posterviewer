from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import requests
import wget

window = Tk()
window.title("Poster Viewer")
window.geometry('500x500')
searched_film = Entry(window, width=25)
searched_film.place(x=0, y=0)

outputdir = filedialog.askdirectory(title="Select a directory to save posters to")

def submit(searched_film, outputdir):
	parameters = {
		"s" : searched_film.get()
	}

	response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=d7209e0", params=parameters)
	poster = response.json()['Search'][0]['Poster']

	wget.download(poster, out=outputdir)
	load_poster = Image.open(outputdir+poster.split("/")[5])
	render_poster = ImageTk.PhotoImage(load_poster)
	poster_img = Label(window, image=render_poster)
	poster_img.image = render_poster
	poster_img.place(x=20, y=40)

btn = Button(window, text="submit", command=lambda: submit(searched_film, outputdir))
btn.place(x=160, y=0)
window.mainloop()