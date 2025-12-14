def rotate_right(pic):
    """
    Rotate the picture 90 degrees to the right (clockwise).
    """
    new_pic = Picture(pic.getHeight(), pic.getWidth())

    for x in range(pic.getWidth()):
        for y in range(pic.getHeight()):
            color = pic.getPixel(x, y)
            new_x = pic.getHeight() - 1 - y
            new_y = x
            new_pic.setPixel(new_x, new_y, color)

    return new_pic
