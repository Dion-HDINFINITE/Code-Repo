print("Selamat datang di pengukur jodoh berdasarkan nama, yang memiliki akurasi yang akurat dan sangat reliable!")
name = input("Nama kao : ")
my_number = 0
for char in name:
    my_number += ord(char)
print("Inisial jodoh kamu adalah : ", chr(my_number % 26 + 65))