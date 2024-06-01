import random
import datetime


class Food:
    random.seed(datetime.datetime.now().timestamp())

    def __init__(self, x_min=0, x_max=550, y_min=0, y_max=550):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.x, self.y = self.generate_random_coordinates()

    def generate_random_coordinates(self):
        x = random.randint(self.x_min, self.x_max)
        y = random.randint(self.y_min, self.y_max)
        return x, y

    def get_new_coordinates(self):
        self.x, self.y = self.generate_random_coordinates()
        return self.x, self.y
