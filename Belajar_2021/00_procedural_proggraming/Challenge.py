a = 0
s = 0
print('Enter Letters to add to the sum.')
print('Enter q to exit.')
while a != "q":
    print('Current Sum:', s)
    s = s + int(a)
    a = (input('Number? '))
print('Total Sum of letters =', s)