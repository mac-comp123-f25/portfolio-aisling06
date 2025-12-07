def red_channel(pic):
    """
    Return a new picture showing only the red channel of the input image.
    The green and blue values are set to 0.
    """
    new_pic = pic.copy()

    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (r, 0, 0))

    return new_pic


def green_channel(pic):
    """
    Return a new picture showing only the green channel of the input image.
    The red and blue values are set to 0.
    """
    new_pic = pic.copy()

    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0, g, 0))

    return new_pic


def blue_channel(pic):
    """
    Return a new picture showing only the blue channel of the input image.
    The red and green values are set to 0.
    """
    new_pic = pic.copy()

    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        new_pic.setColor(x, y, (0, 0, b)) 

    return new_pic
