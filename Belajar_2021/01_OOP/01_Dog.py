
class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.iscute = True
        self.abandoned = True

    def roll_over(self):
        print(f"{self.name} rolled over...")

    def sleep(self):
        print(f"{self.name} : ZZZzzzz")

    def bark(self):
        print(f"{self.name} : Arrrgghhhh")

    def self_destruct(self):
        print(f"{self.name} : Ouchhh")


moly = Dog("moly")
print(moly.name)
print(moly.age)
print(moly.iscute)
moly.roll_over()

print()

holy = Dog("holy")
print(holy.name)
holy.roll_over()
holy.sleep()

print()

Doge = Dog("Doge")
print(Doge.name)
print(Doge.age)
print(Doge.iscute)
print(Doge.abandoned)
Doge.self_destruct()
Doge.roll_over()
Doge.sleep()
Doge.bark()
