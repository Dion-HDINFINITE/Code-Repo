import calendar
from datetime import datetime
import json

from tkinter import Tk, Label, Entry, Button, StringVar, Frame, Radiobutton
from tkinter.ttk import Combobox


def load_data():
	try:
		with open('passengers.json', 'r') as file:
			return json.load(file)
	except:
		return []


def save_data(data):
	with open('passengers.json', 'w') as file:
		json.dump(data, file)


def save_btn():
	name, airline, departure_site, arrival_site, boarding_pass_number = name_var.get(), airline_var.get(), \
							departure_site_var.get(), arrival_site_var.get(), boarding_pass_number_var.get()

	name_entry.focus()
	if name and airline and departure_site:
		student = {
			"name": name,
			"airline": airline,
			"departure_site": departure_site,
			"departure_date": f"{day_var.get()}-{month_var.get()}-{year_var.get()}",
			"arrival_site": arrival_site,
			"arrival_date": f"{day_var.get()}-{month_var.get()}-{year_var.get()}",
			"boarding_pass_number": boarding_pass_number,
			"gender": gender_var.get()
		}
		students.append(student)
		save_data(students)
		name_var.set("")
		departure_site_var.set("")
		arrival_site_var.set("")
		boarding_pass_number_var.set("")
		msg_label.configure(text=" Check in data has been saved ", fg="green")
		return True
	msg_label.configure(text=" Please make sure that all of the data has been filled", fg="red")
	return False


window = Tk()
window.title("  ✈️Airport Check-in Registration  ✈️")
window.geometry("450x550")

title_label = Label(window, text=" ♛ TOTALLY LEGIT AIRPORT ♛ ")
title_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

msg_label = Label(window)
msg_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

name_label = Label(window, text="『Full Name』")
name_label.grid(row=2, column=0, sticky="w")

name_var = StringVar()
name_entry = Entry(window, textvariable=name_var)
name_entry.grid(row=2, column=1, sticky="nsew")

airline_label = Label(window, text=" ✈ Airline Name ✈ ")
airline_label.grid(row=3, column=0, sticky="w")

airline_var = StringVar()
airline_entry = Entry(window, textvariable=airline_var)
airline_entry.grid(row=3, column=1, sticky="nsew")

departure_site_label = Label(window, text=" 🛫 Departure location 🛫 ")
departure_site_label.grid(row=4, column=0, sticky="w")

departure_site_var = StringVar()
departure_site_entry = Entry(window, textvariable=departure_site_var)
departure_site_entry.grid(row=4, column=1, sticky="nsew")

arrival_site_label = Label(window, text=" 🛬 Arrival location 🛬 ")
arrival_site_label.grid(row=5, column=0, sticky="w")

arrival_site_var = StringVar()
arrival_site_entry = Entry(window, textvariable=arrival_site_var)
arrival_site_entry.grid(row=5, column=1, sticky="nsew")

departure_date_label = Label(window, text=" 📅 Departure Date 📅 ")
departure_date_label.grid(row=6, column=0, sticky="w")

departure_date_frame = Frame(window)
departure_date_frame.grid(row=6, column=1, sticky="nsew")

arrival_date_label = Label(window, text=" 📅 Arrival Date 📅 ")
arrival_date_label.grid(row=7, column=0, sticky="w")

arrival_date_frame = Frame(window)
arrival_date_frame.grid(row=7, column=1, sticky="nsew")

boarding_pass_number_label = Label(window, text=" 🎫 Boarding Pass Number 🎫 ")
boarding_pass_number_label.grid(row=8, column=0, sticky="w")

boarding_pass_number_var = StringVar()
boarding_pass_number_entry = Entry(window, textvariable=boarding_pass_number_var)
boarding_pass_number_entry.grid(row=8, column=1, sticky="nsew")

day_var = StringVar()
day_combobox = Combobox(departure_date_frame, width=3, textvariable=day_var)
day_combobox['values'] = list(range(1, 32))
day_combobox.current(datetime.now().day-1)
day_combobox.grid(row=0, column=0, sticky="nsew")

month_var = StringVar()
month_combobox = Combobox(departure_date_frame, width=9, textvariable=month_var)
month_combobox['values'] = list(calendar.month_name)[1:]
month_combobox.current(datetime.now().month-1)
month_combobox.grid(row=0, column=1, sticky="nsew")

year_var = StringVar()
year_combobox = Combobox(departure_date_frame, width=5, textvariable=year_var)
year_combobox['values'] = list(range(2021, 2100))
year_combobox.current(year_combobox['values'].index(str(datetime.now().year)))
year_combobox.grid(row=0, column=2, sticky="nsew")

day_var = StringVar()
day_combobox = Combobox(arrival_date_frame, width=3, textvariable=day_var)
day_combobox['values'] = list(range(1, 32))
day_combobox.current(datetime.now().day-1)
day_combobox.grid(row=0, column=0, sticky="nsew")

month_var = StringVar()
month_combobox = Combobox(arrival_date_frame, width=9, textvariable=month_var)
month_combobox['values'] = list(calendar.month_name)[1:]
month_combobox.current(datetime.now().month-1)
month_combobox.grid(row=0, column=1, sticky="nsew")

year_var = StringVar()
year_combobox = Combobox(arrival_date_frame, width=5, textvariable=year_var)
year_combobox['values'] = list(range(2021, 2100))
year_combobox.current(year_combobox['values'].index(str(datetime.now().year)))
year_combobox.grid(row=0, column=2, sticky="nsew")

gender_label = Label(window, text=" Gender ")
gender_label.grid(row=9, column=0, sticky="w")

gender_frame = Frame(window)
gender_frame.grid(row=9, column=1, sticky="nsew")

gender_var = StringVar()
gender_var.set(" Male ")

maleRb = Radiobutton(gender_frame, text="  ♂️Male  ♂️ ", variable=gender_var, value=" Male ")
maleRb.grid(row=0, column=0, sticky="nsew")

femaleRb = Radiobutton(gender_frame, text="  ♀️Female  ♀️", variable=gender_var, value=" Female ")
femaleRb.grid(row=0, column=1, sticky="nsew")

save_btn = Button(window, text="  ✔️CHECK IN  ✔️", command=save_btn)
save_btn.grid(row=10, column=0, columnspan=2)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

students = load_data()

window.mainloop()
