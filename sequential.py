"""-----------------------------------------------------------------------------
 "
 " File:          Sequential.py
 " Author:        Cody Walker
 " Project:       Parallel Project 1 - n-Bodies and Collisions
 " Description:   A sequential implementation of a simulation of the n-body
 "                gravitational problem written in Python in order to run a
 "                time test between implementations written in different
 "                languages.
 " Created:       12 June 2019
 " Updated:       12 June 2019
 "
 " NOTES:
 "              UNIQUE  |   ORDER   |   CHANGE SPEC EL  |   NEW ELS
 "  LISTS         N           Y                Y               Y
 "  TUPLES        N           Y                N               N
 "  DICT          Y           N                Y               Y
 "  SETS          Y           N                N               Y
 "
 " --------------------------------------------------------------------------"""


"""--------------------------------------------------------------------------"""
"""------------------------------- Globals ----------------------------------"""
"""--------------------------------------------------------------------------"""


pdb = 1     # Debug print statements.

NUM_BODIES = 5          # Number of bodies in the simulation.
TIMESTEPS = 30          # Number of timesteps to be run in simulation.
BODY_RADIUS = 20        # Radius of each body in the simulation.
BODY_MASS = 10000000    # Mass of each body in the simulation.
ENABLE_GUI = 0          # If 1, write coords to file for visual simulation.

xposition = []  # List of x-positions of the bodies.
yposition = []  # List of y-positions of the bodies.
xvelocity = []  # List of x-velocities of the bodies.
yvelocity = []  # List of y-velocities of the bodies.
xforce = []     # List of net x-forces acting upon each of the bodies.
yforce = []     # List of net y-forces acting upon each of the bodies.


"""--------------------------------------------------------------------------"""
"""------------------------------ Functions ---------------------------------"""
"""--------------------------------------------------------------------------"""


"""-----------------------------------------------------------------------------
 " Function:    init
 " Description: Initializes global variables, setting them to be any user-
 "              supplied values if appropriate.
 " Arguments:   argv1 - number of bodies
 "              argv2 - radius of each body
 "              argv3 - number of time steps
 "              argv4 - 1 to enable output for gui, 0 otherwise
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def init():
    # Open file in write mode in order to start fresh.
    with open("testie.txt", "w") as file:
        # Write num_bodies, body_radius, & timesteps to file for GUI.
        file.write(str(NUM_BODIES))
        file.write(" ")
        file.write(str(BODY_RADIUS))
        file.write(" ")
        file.write(str(TIMESTEPS))
        file.write(" ")

    # Close the file.
    file.close()

    # Initialize x & y positions.
    # TODO: ACTUALLY MAKE DIS RANDOM LATER
    for i in range(NUM_BODIES):
        xposition.append(i * 100)
        yposition.append(i * 100)

    # Initialize x & y velocities & forces as 0.
    for _ in range(NUM_BODIES):
        xvelocity.append(0)
        yvelocity.append(0)
        xforce.append(0)
        yforce.append(0)

    return
    """ END init() """


"""-----------------------------------------------------------------------------
 " Function:    print_coordinates
 " Description: Prints out the position coordinates of every body in the
 "              simulation.
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def print_coordinates():
    print("POSITIONS:\n")
    for i in range(NUM_BODIES):
        print("Body", i, "x =", xposition[i], "y =", yposition[i])
    return
    """ END print_coordinates() """


"""-----------------------------------------------------------------------------
 " Function:    print_velocities
 " Description: Prints out the velocities of every body in the simulation.
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def print_velocities():
    print("VELOCITIES:\n")
    for i in range(NUM_BODIES):
        print("Body", i, "vx =", xvelocity[i], "vy =", yvelocity[i])
    return
    """ END print_velocities() """


"""-----------------------------------------------------------------------------
 " Function:    print_forces
 " Description: Prints out the net forces acting upon every body in the
 "              simulation.
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def print_forces():
    print("FORCES:\n")
    for i in range(NUM_BODIES):
        print("Body", i, "x =", xposition[i], "y =", yposition[i])
    return
    """ END print_forces() """


init()
print_coordinates()


"""-----------------------------------------------------------------------------
 " Function:    func
 " Description: desc
 " Arguments:   args
 " Returns:     retval
 " --------------------------------------------------------------------------"""

