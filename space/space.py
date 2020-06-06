#Space Invaders
#Created by Andrea and Carlos
#Python 2.7 on Mac

import turtle
import os

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw a border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("pink")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
#Create the player
player = turtle.Turtle()
player.color("teal")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)







delay = input("Press enter to finish.")