import turtle
n = 5
window = turtle.Screen()
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.color("black", "lightblue")
turtle.begin_fill()
for i in range(n):
    turtle.forward(150)
    turtle.left(360 / n)
turtle.end_fill()

window.exitonclick()
