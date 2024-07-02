import random


class Snake:
    def __init__(self, id, colour):
        self.id = id
        self.colour = colour
        self.size = 1
        self.boost = 0


def colourPicker():
    colours = ["#000000", "#FFFFFF", "#FF0000", "#00FF00", "0000FF"]
    return random.choice(colours)
