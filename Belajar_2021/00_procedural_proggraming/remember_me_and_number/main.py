import json
import random


def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except:
        return {}


def save_data(data_master):
    with open("data.json", "w") as file:
        json.dump(data_master, file)
        return True


def greet_user(data_master):
    username = input("What is your name ? ")
    if username in data_master:
        print(f"Welcome back {username}! ")
    else:
        data_master[username] = None
        save_data(data_master)
        print("We'll remember you when you come back!")
    return user_name


def get_new_favorite_number():
    guessing_number = random.randint(0, 100)
    ans = input(f"i'll")



data_master = load_data()
greet_user(data_master)