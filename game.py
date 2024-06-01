import cellsGUI
import random
import food
import datetime


def newFood():
    f1 = food.Food()
    # time.sleep(0.1)
    # f2 = food.Food()
    # time.sleep(0.1)
    # f3 = food.Food()
    # time.sleep(0.1)
    # f4 = food.Food()

    cellsGUI.drawFood(f1.x, f1.y)

    random.seed(datetime.datetime.now().timestamp())
    cellsGUI.drawFood(random.randint(0, 550), random.randint(0, 550))
    # cellsGUI.drawFood(f3.x, f3.y)
    # cellsGUI.drawFood(f4.x, f4.y)
