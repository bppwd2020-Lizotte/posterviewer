from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import requests
import wget

#~~button command functions
def select_outputdir(dir_label):
	global outputdir
	outputdir = filedialog.askdirectory(title="Select a directory to save posters to")
	display_outputdir = StringVar();
	display_outputdir.set(outputdir)
	dir_label.config(textvariable=display_outputdir)
	
	#allows user to select directory for saving posters

def submit(searched_film, outputdir):
	parameters = {
		"s" : searched_film.get()
		#sets the search term to user input searched_film
	}

	response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=d7209e0", params=parameters)
	poster = response.json()['Search'][0]['Poster']
	#gets json data for searched_film, gets poster link from json data

	wget.download(poster, out=outputdir)
	#downloads poster
	load_poster = Image.open(outputdir+"/"+poster.split("/")[5])
	render_poster = ImageTk.PhotoImage(load_poster)
	poster_img = Label(window, image=render_poster)
	poster_img.image = render_poster
	poster_img.place(x=95, y=70)
	#displays poster in GUI

#~~tkinter GUI
window = Tk()
window.title("Poster Viewer")
window.geometry('500x550')
#basic tkinter setup, window size, title

searched_film = Entry(window, width=70)
searched_film.place(x=5, y=7)
try:
	submit_btn = Button(window, text="submit", command=lambda: submit(searched_film, outputdir))
	submit_btn.place(x=440, y=5)
except NameError:
	error_lable = Label(window, text="YOU NEED TO ENTER A DIRECTORY")
	error_lable.place(x=95, y=70)
#entry for user to input film title and button to submit

dir_label = Label(window)
dir_label.place(x=50, y=32)
selectdir_btn = Button(window, text="open", command=lambda: select_outputdir(dir_label))
selectdir_btn.place(x=5, y=30)
#label to display current directory posters save to and button to open directory selection

window.mainloop()