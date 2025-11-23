import time
from random import randrange
from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import Picture


def get_rand_bg():
    red = randrange(0, 256)
    green = randrange(0, 256)
    blue = randrange(0, 256)

    pic = Picture(100, 100)
    pic.setAllPixels((red, green, blue))
    return pic


def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)

    keep_windows_open()


if __name__ == "__main__":
    main()
