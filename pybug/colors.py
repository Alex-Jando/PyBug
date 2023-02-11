import os

class Color:

    def __init__(self, r: int, g: int, b: int):

        # Line needed to initialise terminal color support. It's a weird bug, but seems to be fixed this way.
        os.system('')

        self.from_rgb(r, g, b)

    def from_rgb(self, r, g, b):

        self.color = f'\033[38;2;{r};{g};{b}m'

    def __add__(self, txt):

        return self.color + txt + '\033[0m'