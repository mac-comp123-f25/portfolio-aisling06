import random

def copy_pic_into_random(small_pic, big_pic):
    small_w = small_pic.getWidth()
    small_h = small_pic.getHeight()
    big_w = big_pic.getWidth()
    big_h = big_pic.getHeight()

    start_x = random.randrange(0, big_w - small_w)
    start_y = random.randrange(0, big_h - small_h)

    for (x, y) in small_pic:
        (r, g, b) = small_pic.getColor(x, y)

        target_x = start_x + x
        target_y = start_y + y

        big_pic.setColor(target_x, target_y, (r, g, b))
