rows = 5
row = 2 * rows - 2
for col in range(0, rows):
    for space in range(0, row):
        print(end=" ")
    row = row - 2
    for space in range(0, col + 1):
        print("* ", end="")
    print("")