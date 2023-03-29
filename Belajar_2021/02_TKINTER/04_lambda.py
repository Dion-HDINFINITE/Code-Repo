from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("more grid")
window.geometry("500x500")

title_label = Label(window, text="More Grid")
title_label.grid(row=0, column=0, columnspan=2,sticky="nsew")

username_label = Label(window, text="Username")
username_label.grid(row=1, column=0, sticky="nsew")

username_entry = Entry(window)
username_entry.grid(row=1, column=1, sticky="nsew")

button = Button(window,
			text="change",
			font=('Comic Sans MS', 20),
			fg="green",
			command = lambda : title_label.configure(text="Okay ..."))

button.grid(row=2, column=0, columnspan=2, sticky="nsew")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()