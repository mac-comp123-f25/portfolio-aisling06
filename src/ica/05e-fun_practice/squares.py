import turtle

def draw_nested_squares(turt):
        for side_length in range(10, 90, 10):
            for reps in range(4):
                turt.forward(side_length)
                turt.left(90)

win = turtle.Screen()
tt = turtle.Turtle()
draw_nested_squares(tt)
win.exitonclick()
