'''
import turtle
import math
panav = turtle.Turtle()
panav.begin_fill()
panav.forward(100)
panav.left(90)
panav.forward(100)
panav.left(90)
panav.forward(100)
panav.left(90)
panav.forward(100)
panav.left(90)
panav.forward(100)

panav.penup()
panav.forward(150)
panav.pendown()

panav.forward(100)
panav.left(90)
panav.forward(100)
panav.left(90)
panav.forward(100)
panav.left(90)
panav.forward(100)
panav.left(90)
panav.forward(100)
panav.end_fill()

panav.color("Red","Yellow")
panav.speed(10)
panav.begin_fill()

for i in range(100):
    panav.forward(300)
    panav.left(169)
panav.end_fill()
turtle.done()
'''
import turtle

def branch(length, t):
    if length > 5:
        t.forward(length)
        t.right(20)
        branch(length - 15, t)
        t.left(40)
        branch(length - 15, t)
        t.right(20)
        t.backward(length)

screen = turtle.Screen()
t = turtle.Turtle()
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
t.speed(0)
branch(100, t)
turtle.done()


