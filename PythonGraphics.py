"""-----------------------------------------------------------------------------
 "
 " File:            PythonGraphics.py
 " Author:          Cody Walker
 " Project:         Parallel Project 1 - n-Bodies and Collisions
 " Description:     Python script to animate the bodies in the N-Body
 "                  Gravitational Simulation.  Reads from graphics_input.txt to
 "                  get the positions of all bodies in each timeframe, and
 "                  draws each time frame one after the other until no more
 "                  remain.
 " Created:         13 June 2019
 " Updated:         17 June 2019
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


# TODO: FIGURE OUT WHETHER OR NOT TO MAKE THIS A CLASS FILE!!!


pdb = 0


bodies = []


with open("graphics_input.txt", "r") as file:
    # First read in how many bodies, radius of each body, & how many timesteps
    # to run the simulation from the .txt file.
    NUM_BODIES = int(file.readline())
    BODY_RADIUS = int(file.readline())
    TIMESTEPS = int(file.readline())

    # Read in world coordinates.
    XMIN = int(file.readline())
    YMIN = int(file.readline())
    XMAX = int(file.readline())
    YMAX = int(file.readline())

    # Read in ENABLE_GUI boolean.
    ENABLE_GUI = int(file.readline())

    if (ENABLE_GUI):
        # Setup viewing window.
        win = turtle.Screen()
        win.bgcolor("black")
        win.title("N-Body Gravitational Simulation")
        turtle.setworldcoordinates(XMIN, YMIN, XMAX, YMAX)


        if (pdb):
            print("NUM_BODIES:", NUM_BODIES, "BODY_RADIUS", BODY_RADIUS,
                  "TIMESTEPS", TIMESTEPS)

        # Add a NUM_BODIES bodies to the bodies list (yes, I know...)
        for _ in range(NUM_BODIES):
            bodies.append(turtle.Turtle())

        # Initialize each body.
        for body in bodies:
            # TODO: figure out how to set radius!!!!!
            body.shape("circle")
            body.color("green")
            # Dont draw path lines.
            body.penup()
            # We will move bodies ourselves, don't let python animate for us.
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
    # END if()

# Dont forget to bring a towel!
file.close()


""" END PythonGraphics.py """
