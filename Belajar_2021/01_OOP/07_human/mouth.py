class Mouth:

    def __init__(self, humaninfo):
        self.human = humaninfo

    def describe_about_sex(self):
        print(f"I am {self.human.sex}")