n = 6
import turtle
window = turtle.Screen()
poly_turle = turtle.Turtle()
poly_turle.color("blue")
poly_turle.shape("turtle")
for reps in range(n):
    poly_turle.forward(180)
    poly_turle.right(360/n)
window.exitonclick()