import cellsGUI
import time
import game


def main():
    i = 0
    while i < 8:
        game.newFood()
        cellsGUI.drawFrame()
        # time.sleep(1)
        i += 1
        # time.sleep(0.8)


main()
