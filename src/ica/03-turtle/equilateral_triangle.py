import turtle
window = turtle.Screen()
tria_turtle = turtle.Turtle()
tria_turtle.color("purple")
tria_turtle.shape("turtle")

tria_turtle.begin_fill()
for reps in range(3):
    tria_turtle.forward(90)
    tria_turtle.left(120)
tria_turtle.end_fill()

window.exitonclick()