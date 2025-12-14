def weighted_scale(pic, w1, w2, w3):
    """
    Create a weighted grayscale version of the picture.
    Each pixel's luminance is computed as w1*r + w2*g + w3*b.

    :param pic: The original Picture object
    :param w1: weight for red channel (0.0 to 1.0)
    :param w2: weight for green channel (0.0 to 1.0)
    :param w3: weight for blue channel (0.0 to 1.0)
    :return: a new Picture object (weighted grayscale)
    """
    new_pic = pic.copy()

    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)

        lumin = w1 * r + w2 * g + w3 * b

        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

