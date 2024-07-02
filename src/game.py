from snake import Snake, colourPicker
import snake


snakes = []


def newSnake():
    snakes.append(Snake(len(snakes), colourPicker()))


def run():
    for i in range(0, 5):
        newSnake()
        print(snakes[i].colour)


temp = []
