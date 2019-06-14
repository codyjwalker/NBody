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

            # TODO: SPEED UP WITH DISTANCES LIST OR SUM10


import math
import time

# Test for gcommit


"""--------------------------------------------------------------------------"""
"""------------------------------- Globals ----------------------------------"""
"""--------------------------------------------------------------------------"""


pdb = 1     # Debug print statements.

NUM_BODIES = 4          # Number of bodies in the simulation.
TIMESTEPS = 30          # Number of timesteps to be run in simulation.
BODY_RADIUS =  5        # Radius of each body in the simulation.
BODY_MASS = 100000000   # Mass of each body in the simulation.
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
            ydirection = yposition[j] - yposition[i]
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
 " Function:    collisions_detected
 " Description: Checks the current state of the simulation, and determines
 "              whether or not the previous movement calculation has caused any
 "              collisions to occur.
 " Arguments:   None.
 " Returns:     1 if any collisions have occured, 0 otherwise.
 " --------------------------------------------------------------------------"""
def collisions_detected():
    is_collision = 0    # Boolean representing if collision occurred.
    for i in range(NUM_BODIES - 1):
        for j in range(i + 1, NUM_BODIES):
            # TODO: SPEED UP WITH DISTANCES LIST OR SUM10
            # Calculate distance between current pair of bodies.
            x_dist_chunk = (xposition[i] - xposition[j]) * (xposition[i] -
                                                            xposition[j])
            y_dist_chunk = (yposition[i] - yposition[j]) * (yposition[i] -
                                                            yposition[j])
            distance = math.sqrt(x_dist_chunk + y_dist_chunk)
            if (distance < (2 * BODY_RADIUS)):
                if (pdb):
                    print("\nCOLLISION!!!!!!!\n")
                # Mark that these two objects in particular collided.
                collisions.append((i,j))
                is_collision = 1
    return is_collision
    """ END collisions_detected() """


"""-----------------------------------------------------------------------------
 " Function:    resolve_collisions
 " Description: Called when two or more objects are in a "state of collision"
 "              to properly determine their new velocities and positions
 "              resulting from them colliding.  Without this method, not only
 "              would objects pass through eachother, but because the
 "              magnitude of the force of gravity becomes exponentially larger
 "              the closer together bodies get, the bodies would become under
 "              tremendous force and fly off at comical speeds in the direction
 "              they were just heading.  Very important function.
 "              NOTE:
 "              THE PROCEDURES USED TO CALCULATE THE FINAL VELOCITIES OF THE
 "              OBJECTS ARE TAKEN FROM DR. HOMER'S HANDOUT WHICH IS BADED ON
 "              "2-Dimensional Elastic Collisions Without Trigonometry" by
 "              Chad Bercheck, AND IS NOT MY OWN ORIGINAL MATERIAL.
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def resolve_collisions():
    # Handle every collision that occurred in current timestep.
    while (len(collisions) > 0):
        # First, get the two bodies involved in current collision.
        curr = collisions.pop()
        body1 = curr[0]
        body2 = curr[1]
        if (pdb):
            print("body1:", body1, "  ", "body2:", body2)

        # Extract information about velocities and positions of bodies.
        x1 = xposition[body1]
        y1 = yposition[body1]
        x2 = xposition[body2]
        y2 = yposition[body2]
        v1x = xvelocity[body1]
        v1y = yvelocity[body1]
        v2x = xvelocity[body2]
        v2y = yvelocity[body2]

        # Precompute simm. chunks used in all equations - reduce computations.
        denom = ((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))
        chunk1 = (v1y * (x2 - x1) * (y2 - y1))
        chunk2 = (v2y * (x2 - x1) * (y2 - y1))
        chunk3 = (v1x * (y2 - y1) * (x2 - x1))
        chunk4 = (v2x * (x2 - x1) * (y2 - y1))

        # Determine final x velocity of first body.
        v1fx = v2x * (x2 - x1) * (x2 - x1)
        v1fx = v1fx + chunk2
        v1fx = v1fx + (v1x * (y2 - y1) * (y2 - y1))
        v1fx = v1fx - chunk1
        v1fx = v1fx / denom

        # Determine final y velocity of first body.
        v1fy = chunk4
        v1fy = v1fy + (v2y * (y2 - y1) * (y2 - y1))
        v1fy = v1fy - chunk3
        v1fy = v1fy + (v1y * (x2 - x1) * (x2 - x1))
        v1fy = v1fy / denom

        # Determine final x velocity of second body.
        v2fx = v1x * (x2 - x1) * (x2 - x1)
        v2fx = v2fx + chunk1
        v2fx = v2fx + (v2x * (y2 - y1) * (y2 - y1))
        v2fx = v2fx - chunk2
        v2fx = v2fx / denom

        # Determine final y velocity of second body.
        v2fy = chunk3
        v2fy = v2fy + (v1y * (y2 - y1) * (y2 - y1))
        v2fy = v2fy - chunk4
        v2fy = v2fy + (v2y * (x2 - x1) * (x2 - x1))
        v2fy = v2fy / denom

        # Determine final positions of bodies.
        xposition[body1] = xposition[body1] + v1fx
        yposition[body1] = yposition[body1] + v1fy
        xposition[body2] = xposition[body2] + v2fx
        yposition[body2] = yposition[body2] + v2fy

        # Copy new velocities into global lists.
        xvelocity[body1] = v1fx
        yvelocity[body1] = v1fy
        xvelocity[body2] = v2fx
        yvelocity[body2] = v2fy

    return
    """ END resolve_collisions() """


"""-----------------------------------------------------------------------------
 " Function:    export_positions
 " Description: Writes the information contained inside the position array at
 "              the current timeframe to a .txt file for a GUI to read and
 "              use to generate a visualization of the simulation.
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def export_positions():
    # TODO: IMPLEMENT THIS METHOD
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
    print("\nPOSITIONS:")
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


"""-----------------------------------------------------------------------------
 " Function:    print_collisions
 " Description: Prints out the tuples that are currently in the collision list.
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def print_collisions():
    print("COLLISIONS:")
    for collision in collisions:
        print("COLLISION between bodies: ", collision)
    return
    """ END print_collisions() """


"""-----------------------------------------------------------------------------
 " Function:    main
 " Description: Doesn't do much, just calls functions to do all the work
 "              instead.  Records system time before and after doing the work
 "              to be used for measurement of execution time.
 " Arguments:   argv1 - number of bodies
 "              argv2 - radius of each body
 "              argv3 - number of time steps
 "              argv4 - 1 to enable output for gui, 0 otherwise
 "              argv5 - number of dimensions to run simulation in (2 or 3)
 " Returns:     Appropriate exit status of program.
 " --------------------------------------------------------------------------"""
def main():

    # TODO: Time calculation bs

    start_time = time.perf_counter()

    init()
    if (pdb):
        print_coordinates()

    # Run Simulation for # of timesteps requested.
    for i in range(TIMESTEPS):

        # Calculate net force acting on each body.
        calculate_forces()

        # Move bodies appropriately based upon the net force acting upon them.
        move_bodies()

        # Check for collisions and resolve any that are found.
        if (collisions_detected()):
            if(pdb):
                print_collisions()
            resolve_collisions()
            if(pdb):
                print_collisions()

        # If print debug variable turned on, print to stdout.
        if (pdb):
            print_coordinates()

        # If GUI mode enabled write positions to file.
        if (ENABLE_GUI):
            export_positions()

    end_time = time.perf_counter()
    print("\n\nTOTAL TIME ELAPSED:   ", end_time - start_time, "\n\n")

    return
    """ END main() """


# The call to main() that gets the whole simulation started.
main()


"""-----------------------------------------------------------------------------
 " Function:    func
 " Description: desc
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""

""" END sequential.py """
