def color_shuffle(pic):
    """
    Return a new picture with color channels shuffled:
    R -> G, G -> B, B -> R.

    For example: (R, G, B) becomes (B, R, G).

    :param pic: The original Picture object
    :return: A new Picture object with shuffled color channels
    """
    new_pic = pic.copy()

    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)

        new_color = (b, r, g)

        new_pic.setColor(x, y, new_color)

    return new_pic
