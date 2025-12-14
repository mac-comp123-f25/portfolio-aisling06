from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *
def copy_pic_into(small_pic, big_pic, start_x, start_y):
    for (x,y) in small_pic:
        (r, g, b) = small_pic.getColor(x, y)
        target_x = x + start_x
        target_y = y + start_y
        big_pic.setColor(target_x, target_y, (r, g, b))

green_turtle = Picture("../SampleImages/greenTurtle.jpg")
scene = Picture("../SampleImages/bearLake.jpg")
copy_pic_into(green_turtle, scene, 25, 25)
copy_pic_into(green_turtle, scene, 200, 200)
copy_pic_into(green_turtle, scene, 400, 200)
scene.show()

keep_windows_open()


