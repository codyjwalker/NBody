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


pdb = 1


bodies = []


win = turtle.Screen()
win.bgcolor("black")
win.title("N-Body Gravitational Simulation")


with open("gui_input.txt", "r") as file:
#with open("py_gui_input.txt", "r") as file:
    # First read in how many bodies, radius of each body, & how many timesteps
    # to run the simulation from the .txt file.
    NUM_BODIES = int(file.readline())
    BODY_RADIUS = int(file.readline())
    TIMESTEPS = int(file.readline())

    if (pdb):
        print("NUM_BODIES:", NUM_BODIES, "BODY_RADIUS", BODY_RADIUS, "TIMESTEPS",
              TIMESTEPS)

    # Add a NUM_BODIES bodies to the bodies list (yes, I know...)
    for _ in range(NUM_BODIES):
        bodies.append(turtle.Turtle())

    # Initialize each body.
    for body in bodies:
        body.shape("circle")
        body.color("green")
        # Dont draw path lines.
        body.penup()
        # We will move the bodies ourselves, don't let python animate for us.
        body.speed(0)


    # Keep going until all timesteps have been animated.
    for _ in range(TIMESTEPS):
        # Animate each body.
        for body in bodies:
            xpos = float(file.readline())
            ypos = float(file.readline())
            if (pdb): print("xpos:", xpos, "ypos:", ypos)
            body.goto(xpos, ypos)

    # To prevent everything from crashing.
    turtle.done()

# Dont forget to bring a towel!
file.close()






""" END PythonGraphics.py """
