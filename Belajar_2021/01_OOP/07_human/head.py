from eye import Eye
from mouth import Mouth


class Head:

    def __init__(self, humaninfo):
        self.human = humaninfo
        self.eyes = Eye()
        self.mouth = Mouth(self.human)