"""
This program was made by :
Name : Dion Febrian Halim
Class : 10
"""


import os
import random


def intro():
    try:
        os.system("cls")
        print("Welcome to Battleship, you low life nerds")
        res = int(input("Enter the amount of rows you wanna play : "))

        if res < 3 or res > 10:
            print()



def setting_up_board(rows):

    board = []

    for row in range(rows):
        line = []
        for items in range(rows):
            line.append("■")
        board.append(line)

    return board


def setting_up_ship_location(rows):
    location = str(random.randint(0, rows-1)), str(random.randint(0, rows-1))
    return list(location)


def printing_board(board):
    os.system("cls")
    for row in board:
        for item in row:
            print(item, end=" ")
        print()


def check_user_input():
    try:
        user_input = input("Enter ship location : ").split(" ")
    except ValueError as e:
        print(f"You must input an integer!\nPython Error:{e}")
        input("Enter to try again")
        return check_user_input()
    else:
        if len(user_input) != 2:
            return check_user_input()
        user_input = [str(int(user_input[0])-1), str(int(user_input[1])-1))]

    if my_ship == user_input:
        return True

    my_board[int(user_input[0])][int(user_input[1])] = "X"
    return False


def congrats():
    print(f"Congratulations! you win the game with {attempt} attempts")


Win = False
attempt = 1

rows = intro()
print(rows)

"""""
my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)
 
while not Win:
 
    printing_board(my_board)
    print(my_ship)
    Win = check_user_input()
    if not Win:
        attempt += 1
 
congrats()
"""
