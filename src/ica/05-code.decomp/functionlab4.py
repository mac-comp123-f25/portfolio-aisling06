
import turtle
import math

def drawFiveCircles(turt, radius, centerX, centerY):
    """
    Draws five circles arranged around a center point.
    Inputs:
      turt = the turtle to draw with
      radius = the size of each circle
      centerX, centerY = the coordinates of the center
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
      Inputs:
        turt    - the turtle that will do the drawing
        centerX - x coordinate of the flower’s center
        centerY - y coordinate of the flower’s center
      """
    turt.up()
    turt.goto(centerX, centerY - 15)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()


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

drawFiveCircles(sepalTurtle, 50, 0, 0)
drawFiveCircles(petalTurtle, 25, 0, 0)

drawCenterCircle(centerTurtle, 0, 0)

stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, 0, 220)
drawFiveCircles(petalTurtle, 25, 0, 220)

drawCenterCircle(centerTurtle, 0, 220)

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, 220, 0)
drawFiveCircles(petalTurtle, 25, 220, 0)

drawCenterCircle(centerTurtle, 220, 0)

stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, 0, -220)
drawFiveCircles(petalTurtle, 25, 0, -220)

drawCenterCircle(centerTurtle, 0, -220)

stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle, 50, -220, 0)
drawFiveCircles(petalTurtle, 25, -220, 0)

drawCenterCircle(centerTurtle, -220, 0)

stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()