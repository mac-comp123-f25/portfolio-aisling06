import turtle

def spiral_in(turt, side_len):
    if side_len < 5:
        return

    turt.forward(side_len)
    turt.right(90)

    spiral_in(turt, side_len - 5)


def check_spiral_in(start_len):
    wn = turtle.Screen()
    wn.setworldcoordinates(-10, -10, start_len + 10, start_len + 10)
    turt = turtle.Turtle()
    turt.speed(0)
    spiral_in(turt, start_len)
    wn.exitonclick()


# check_spiral_in(200)

