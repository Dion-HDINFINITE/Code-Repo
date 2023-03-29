
from tkinter import Tk, Label, Entry, Button

window = Tk()

label = Label(window, text="I Love You 3000")
label.grid()

entry = Entry(window)
entry.grid()

button = Button(window, text="submit!")
button.grid()

window.mainloop()