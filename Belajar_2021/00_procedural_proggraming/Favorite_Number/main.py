import json
import random


def saving_data(favorite_number):
    with open("data.json", "w") as file:
        json.dump(favorite_number, file)


def loading_data():
    with open("data.json", "r") as file:
        return json.load(file)


def get_stored_number():
    try:
        return loading_data()
    except:
        return


def get_by_guessing():
    guessing_favorite_number = random.randint(0, 100)
    confirm_ans = input(f"i'll guess your favorite number is {guessing_favorite_number}, is it right? (y/n)")
    if confirm_ans.lower() == "y":
        return str(guessing_favorite_number)


def get_new_favorite_number():
    guessing_favorite_number = get_by_guessing()
    if guessing_favorite_number:
        favorite_number = guessing_favorite_number
    else:
        favorite_number = input("So, what is your favorite number? ")

    saving_data(favorite_number)
    return favorite_number


def ask_user():
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"I know your favorite number, it's {favorite_number}")
    else:
        favorite_number = get_new_favorite_number()
        print(f"I'll remember", {favorite_number}, " as your favorite number")


ask_user()
