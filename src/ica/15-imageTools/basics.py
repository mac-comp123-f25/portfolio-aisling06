from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

pic3 = Picture("../SampleImages/bryceCanyon.jpg")
pic3.show()
pic3_copy = pic3.copy()
width = pic3_copy.getWidth()
height = pic3_copy.getHeight()
red = (255, 0, 0)
pic3_copy.setColor(0,0,red)
pic3_copy.setColor(width-1, 0, red)
pic3_copy.setColor(0,height-1, red)
pic3_copy.setColor(width-1, height-1, red)
pic3_copy.save("../SampleImages/mightyMidway-redCorners.jpg")
pic3_copy.explore()

keep_windows_open()

