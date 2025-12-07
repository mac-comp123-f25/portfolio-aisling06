from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def crop_picture(pic, crop_x, crop_y, width, height):
    new_pic = Picture(width, height)
    for (x, y) in new_pic:
        new_x = x + crop_x
        new_y = y + crop_y
        (r, g, b) = pic.getColor(new_x, new_y)
        new_pic.setColor(x, y, (r, g, b))
    return new_pic

dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam_crop1.show()
dam_crop2.show()
keep_windows_open()