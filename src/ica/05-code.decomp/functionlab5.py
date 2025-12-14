
import turtle
import math

def drawFlower(st, pt, ct, stp, centerX, centerY):
    """
    Draws a complete flower with sepals, petals, a center circle, and a bee.
    """
    drawFiveCircles(st, 50, centerX, centerY)
    drawFiveCircles(pt, 25, centerX, centerY)
    drawCenterCircle(ct, centerX, centerY)
    drawBee(stp, centerX, centerY)

def drawFiveCircles(turt, radius, centerX, centerY):
    """
    Draws five circles arranged around a center point.
    """
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for reps in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

def drawCenterCircle(turt, centerX, centerY):
    """
    Draw the center circle of a flower.
    """
    turt.up()
    turt.goto(centerX, centerY - 15)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()

def drawBee(turt, centerX, centerY):
    """
    Stamp a honeybee in the middle of a flower.
    """
    turt.up()
    turt.goto(centerX - 2, centerY)
    turt.down()
    turt.stamp()

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 0)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 220)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 220, 0)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, -220)
drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, -220, 0)

win.exitonclick()