import turtle
from turtle import Screen
from math import sqrt, pi, sin, cos

screen = Screen()

turtle.hideturtle()
turtle.speed('fastest')
turtle.shape("arrow")
turtle.up()
turtle.color("black")
turtle.width(5)


def spiral():
    turtle.home()
    turtle.clear()
    turtle.down()

    for j in range(200):
        t = j / 20 * pi
        dx = (1 + 5 * t) * cos(t)
        dy = (1 + 5 * t) * sin(t)

        turtle.goto(0 + dx, 0 + dy)
    turtle.up()


def square_spiral(a):
    turtle.home()
    turtle.clear()
    turtle.down()

    step = a / 10
    for i in range(1, 11):
        for j in range(2):
            turtle.forward(step * i)
            turtle.left(90)
    turtle.up()


def square(a):
    turtle.home()
    turtle.clear()
    turtle.down()

    turtle.penup()
    turtle.goto(- a / 2, a / 2)
    turtle.pendown()
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.up()


def circle(r):
    turtle.home()
    turtle.clear()
    turtle.down()

    turtle_step = 2 * pi * r / 360
    turtle.penup()
    turtle.goto(r / 2, 0)
    turtle.pendown()
    turtle.right(90)
    for i in range(180):
        turtle.forward(turtle_step)
        turtle.right(2)
    turtle.up()


def triangle(a):
    turtle.home()
    turtle.clear()
    turtle.down()

    turtle.penup()
    turtle.goto(-a / 2, -(a / 2 * sqrt(3) / 3))
    turtle.pendown()
    for i in range(3):
        turtle.forward(a)
        turtle.left(120)
    turtle.up()


def hexagon(a):
    turtle.home()
    turtle.clear()
    turtle.down()

    turtle.penup()
    turtle.goto(-a / 2, -a * sqrt(3) / 2)
    turtle.pendown()
    for i in range(6):
        turtle.forward(a)
        turtle.left(60)
    turtle.up()


def cursor(a):
    turtle.home()
    turtle.clear()
    turtle.left(90)
    turtle.forward(a / 2)
    turtle.left(90)
    turtle.forward(a / 2)
    turtle.left(180)
    turtle.pendown()

    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a / 2 * sqrt(2))
    turtle.right(90)
    turtle.forward(a / 2 * sqrt(2))
    turtle.right(75)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)

    turtle.penup()
    turtle.forward(a / 2)
    turtle.right(90)
    turtle.forward(sqrt(3) / 2 * a)

    turtle.pendown()
    turtle.right(180)
    turtle.forward(sqrt(3) / 2 * a + a / 2)
    turtle.up()


def star(a):
    turtle.home()
    turtle.clear()
    turtle.down()

    for i in range(8):
        turtle.left(90)
        turtle.forward(a / 2)
        turtle.left(90)
        turtle.forward(a / 2)
        turtle.left(180)
        turtle.pendown()

        turtle.forward(a)
        turtle.right(135)
        turtle.forward(a / 2 * sqrt(2))
        turtle.right(90)
        turtle.forward(a / 2 * sqrt(2))
        turtle.right(75)
        turtle.forward(a)
        turtle.right(120)
        turtle.forward(a)
        turtle.right(120)

        turtle.penup()
        turtle.forward(a / 2)
        turtle.right(90)
        turtle.forward(sqrt(3) / 2 * a)

        turtle.pendown()
        turtle.right(180)
        turtle.forward(sqrt(3) / 2 * a + a / 2)
        turtle.right(360 / 8)
    turtle.up()


def duck():
    turtle.home()
    turtle.clear()
    turtle.pendown()
    turtle.color("black", "yellow")
    turtle.begin_fill()
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(180)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(20)
    turtle.left(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(15)
    turtle.right(45)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)

    for i in range(2):
        turtle.forward(30)
        turtle.right(45)
        turtle.forward(20)
        turtle.left(45)
        turtle.forward(20)
        turtle.left(45)
        turtle.forward(20)
        turtle.left(45)
        turtle.forward(21)
        turtle.left(45)
        turtle.forward(125)
        turtle.left(45)
        turtle.forward(25)
        turtle.left(135)
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(40)
        turtle.left(45)
        turtle.forward(25)
        turtle.left(135)
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(40)
        turtle.left(45)
        turtle.forward(25)
        turtle.left(135)
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(40)
        turtle.left(45)
        turtle.forward(24)
        turtle.left(135)
        turtle.forward(155)
        turtle.left(45)

    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(40)
    turtle.left(45)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(40)
    turtle.left(45)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(30)
    turtle.end_fill()
    turtle.color("black", "orange")
    turtle.begin_fill()
    turtle.left(135)
    turtle.penup()
    turtle.forward(105)
    turtle.pendown()
    turtle.forward(75)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(35)
    turtle.left(180)
    turtle.forward(35)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(45)
    turtle.forward(30)
    turtle.end_fill()
    turtle.penup()
    turtle.left(45)
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.up()


x = 100
screen.listen()
screen.onkeyrelease(lambda: square(x), "1")
screen.onkeyrelease(lambda: circle(x), "2")
screen.onkeyrelease(lambda: triangle(x), "3")
screen.onkeyrelease(lambda: hexagon(x), "4")
screen.onkeyrelease(lambda: spiral(), "5")
screen.onkeyrelease(lambda: square_spiral(x), "6")
screen.onkeyrelease(lambda: cursor(x), "7")
screen.onkeyrelease(lambda: star(x), "8")
screen.onkeyrelease(lambda: duck(), "9")
screen.onkeyrelease(lambda: turtle.bye(), "x")
turtle.done()
