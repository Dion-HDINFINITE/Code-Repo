from random import choice


class Eye:

    def __init__(self):
        self.color = "Black"
        self.is_big = True
        self.number = 2


class Head:

    def __init__(self):
        self.eyes = Eye()


class Human:

    def __init__(self, name):

        self.name = name
        self.age = 0
        self.sex = choice(["Male", "Female", "Not sure"])

        self.head = Head()

    def describe_me(self):
        print(f"Hello, I'm {self.name}, and now {self.age} years old")


jordan = Human("Jordan")
print(jordan.head.eyes.color)

jesse = Human("Jesse")
print(jesse.head.eyes.color)

stefani = Human("Stefani")
print(stefani.head.eyes.color)