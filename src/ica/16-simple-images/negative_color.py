def negative(pic):
    """
    Create and return a negative version of the input picture.
    Each pixel's RGB value is flipped: new_value = 255 - old_value.

    :param pic: The original Picture object
    :return: A new Picture object (negative of the input)
    """
    new_pic = pic.copy()

    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)

        new_r = 255 - r
        new_g = 255 - g
        new_b = 255 - b

        new_pic.setColor(x, y, (new_r, new_g, new_b))

    return new_pic


