"""-----------------------------------------------------------------------------
 "
 " File:            PythonGraphics.py
 " Author:          Cody Walker
 " Project:         Parallel Project 1 - n-Bodies and Collisions
 " Description:     Python script to animate the bodies in the N-Body
 "                  Gravitational Simulation.  Reads from py_gui_input.txt to
 "                  get the positions of all bodies in each timeframe, and
 "                  draws each time frame one after the other until no more
 "                  remain.
 " Created:         13 June 2019
 " Updated:         13 June 2019
 "
 " NOTES:
 "              UNIQUE  |   ORDER   |   CHANGE SPEC EL  |   NEW ELS
 "  LISTS         N           Y                Y               Y
 "  TUPLES        N           Y                N               N
 "  DICT          Y           N                Y               Y
 "  SETS          Y           N                N               Y
 "
 " --------------------------------------------------------------------------"""


import turtle


win = turtle.Screen()
win.bgcolor("black")
win.title("N-Body Gravitational Simulation")


body = turtle.Turtle()
body.shape("circle")
body.color("green")
# Dont draw path lines.
body.penup()
# We will move the bodies ourselves, don't let python animate for us.
body.speed(0)
body.goto(0, 200)


# To prevent everything from crashing.
turtle.done()


""" END PythonGraphics.py """
