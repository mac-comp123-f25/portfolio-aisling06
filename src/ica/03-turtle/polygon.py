n = 6
import turtle
window = turtle.Screen()
poly_turtle = turtle.Turtle()
poly_turtle.color("blue")
poly_turtle.shape("turtle")
for reps in range(n):
    poly_turtle.forward(180)
    poly_turtle.right(360/n)
window.exitonclick()