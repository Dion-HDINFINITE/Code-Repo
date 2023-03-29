import calendar
from datetime import datetime
import json

from tkinter import Tk, Label, Entry, Button, StringVar, Frame, Radiobutton
from tkinter.ttk import Combobox

def load_data():
	pass

def save_data():
	pass

def save_btn():
	pass

window = Tk()
window.title("Form Pendaftaran Siswa Ignatius Global School")
window.geometry("300x400")

title_label = Label(window, text="Ignatius Global School")
title_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

name_label = Label(window, text="Nama Lengkap")
name_label.grid(row=1, column=0, sticky="w")

name_var = StringVar()
name_entry = Entry(window, textvariable=name_var)
name_entry.grid(row=1, column=1, sticky="nsew")

origin_label = Label(window, text="Sekolah Asal")
origin_label.grid(row=2, column=0, sticky="w")

origin_var = StringVar()
origin_entry = Entry(window, textvariable=origin_var)
origin_entry.grid(row=2, column=1, sticky="nsew")

birth_place_label = Label(window, text="Tempat Lahir")
birth_place_label.grid(row=3, column=0, sticky="w")

birth_place_var = StringVar()
birth_place_entry = Entry(window, textvariable=birth_place_var)
birth_place_entry.grid(row=3, column=1, sticky="nsew")

birth_date_label = Label(window, text="Tanggal Lahir")
birth_date_label.grid(row=4, column=0, sticky="w")

birth_date_frame = Frame(window)
birth_date_frame.grid(row=4, column=1, sticky="nsew")

day_var = StringVar()
day_combobox = Combobox(birth_date_frame, width=3, textvariable=day_var)
day_combobox['values'] = list(range(1,32))
day_combobox.current(datetime.now().day-1)
day_combobox.grid(row=0, column=0, sticky="nsew")

month_var = StringVar()
month_combobox = Combobox(birth_date_frame, width=9, textvariable=month_var)
month_combobox['values'] = list(calendar.month_name)[1:]
month_combobox.current(datetime.now().month-1)
month_combobox.grid(row=0, column=1, sticky="nsew")

year_var = StringVar()
year_combobox = Combobox(birth_date_frame, width=5, textvariable=year_var)
year_combobox['values'] = list(range(2000,2022))
#year_combobox.current(datetime.now().year-2000)
year_combobox.current(year_combobox['values'].index(str(datetime.now().year)))
year_combobox.grid(row=0, column=2, sticky="nsew")

jk_label = Label(window, text="Jenis Kelamin")
jk_label.grid(row=5, column=0, sticky="w")

jk_frame = Frame(window)
jk_frame.grid(row=5, column=1, sticky="nsew")

jk_var = StringVar()
jk_var.set("Laki-laki")

maleRb = Radiobutton(jk_frame, text="Laki-laki", variable=jk_var, value="Laki-laki")
maleRb.grid(row=0, column=0, sticky="nsew")

femaleRb = Radiobutton(jk_frame, text="Perempuan", variable=jk_var, value="Perempuan")
femaleRb.grid(row=0, column=1, sticky="nsew")

save_btn = Button(window, text="save data")
save_btn.grid(row=6, column=0, columnspan=2)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()