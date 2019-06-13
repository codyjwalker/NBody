"""-----------------------------------------------------------------------------
 "
 " File:          sequential.py
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


import math


"""--------------------------------------------------------------------------"""
"""------------------------------- Globals ----------------------------------"""
"""--------------------------------------------------------------------------"""


pdb = 1     # Debug print statements.

NUM_BODIES = 5          # Number of bodies in the simulation.
TIMESTEPS = 30          # Number of timesteps to be run in simulation.
BODY_RADIUS = 20        # Radius of each body in the simulation.
BODY_MASS = 10000000    # Mass of each body in the simulation.
ENABLE_GUI = 0          # If 1, write coords to file for visual simulation.

GRAV_CONST = 6674.08    # G scaled by 1000 to make numbers easier to work with.
SPECIAL_G = 2 * GRAV_CONST * BODY_MASS  # To lessen number of computations.

xposition = []  # List of x-positions of the bodies.
yposition = []  # List of y-positions of the bodies.
xvelocity = []  # List of x-velocities of the bodies.
yvelocity = []  # List of y-velocities of the bodies.
xforce = []     # List of net x-forces acting upon each of the bodies.
yforce = []     # List of net y-forces acting upon each of the bodies.

collisions = [] # List of collisions that occurred in current timestep.


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

    # TODO: take command line args?

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
 " Function:    calculate_forces
 " Description: For each body, calculates the net force acting upon it from all
 "              the other bodies in the simulation in the current timeframe.
 "              The function does not move any of the bodies, and merely does
 "              the calculations for all the forces at the current moment in
 "              time.
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def calculate_forces():

    for i in range(NUM_BODIES - 1):
        # Start j at i + i since we save the forces to BOTH bodies each iter.
        for j in range(i + 1, NUM_BODIES):
            # Calculate distance between current pair of bodies.
            x_dist_chunk = (xposition[i] - xposition[j]) * (xposition[i] -
                                                            xposition[j])
            y_dist_chunk = (yposition[i] - yposition[j]) * (yposition[i] -
                                                            yposition[j])
            distance = math.sqrt(x_dist_chunk + y_dist_chunk)
            # Calculate magnitude of gravitational force between pair of bodies
            magnitude = SPECIAL_G / (distance * distance)
            # Precompute some shunks to lessen total # of computations.
            xdirection = xposition[j] - xposition[i]
            ydirection = yposition[j] = yposition[i]
            mag_over_dist = (magnitude / distance)
            x_chunk = (mag_over_dist * xdirection)
            y_chunk = (mag_over_dist * ydirection)
            # Save BOTH forces to cut calculations in half.
            xforce[i] = xforce[i] + x_chunk
            xforce[j] = xforce[j] - x_chunk
            yforce[i] = yforce[i] + y_chunk
            yforce[j] = yforce[j] - y_chunk
    return
    """ END calculate_forces() """


"""-----------------------------------------------------------------------------
 " Function:    move_bodies
 " Description: For each body, determines first its new velocity as a result of
 "              the net forct acting upon it, and then its new position as a
 "              result of its new velocity.
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def move_bodies():
    for i in range(NUM_BODIES):
        # Calculate change in velocity resulting from net force on current obj.
        x_delta_v = xforce[i] / BODY_MASS
        y_delta_v = yforce[i] / BODY_MASS
        # Calculate change in position resulting from curr object's velocity.
        x_delta_p = xvelocity[i] + (x_delta_v * 0.5)
        y_delta_p = yvelocity[i] + (y_delta_v * 0.5)
        # Store current object's new velocity.
        xvelocity[i] = xvelocity[i] + x_delta_v
        yvelocity[i] = yvelocity[i] + y_delta_v
        # Store current object's new position.
        xposition[i] = xposition[i] + x_delta_p
        yposition[i] = yposition[i] + y_delta_p
        # Reset force vector to prepare for next time move_bodies called.
        xforce[i] = 0
        yforce[i] = 0
    return
    """ END move_bodies() """


"""-----------------------------------------------------------------------------
 " Function:    func
 " Description: desc
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def export_positions():
    return
    """ END export_positions() """




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
if (pdb):
    print_coordinates()

# Run Simulation for # of timesteps requested.
for i in range(TIMESTEPS):

    # Calculate net force acting on each body.
    calculate_forces()

    # Move bodies appropriately based upon the net force acting upon them.
    move_bodies()
    
    # If print debug variable turned on, print to stdout.
    if (pdb):
        print_coordinates()

    # If GUI mode enabled write positions to file.
    if (ENABLE_GUI):
        export_positions()




"""-----------------------------------------------------------------------------
 " Function:    func
 " Description: desc
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""

""" END sequential.py """
