import turtle
window = turtle.Screen()
star1 = turtle.Turtle()
star1.color("yellow")
star1.shape("turtle")

for reps in range(5):
    star1.forward(70)
    star1.right(144)

star2 = turtle.Turtle()
star2.color("orange")
star2.shape("turtle")
star2.penup()
star2.goto(100,100)
star2.pendown()

for reps in range(5):
    star2.forward(70)
    star2.right(144)

window.exitonclick()