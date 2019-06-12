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
 " --------------------------------------------------------------------------"""

import SequentialModule as SM


pdb = 1 # Debug print statements.


"""--------------------------------------------------------------------------"""
"""----------------------------- Functions ----------------------------------"""
"""--------------------------------------------------------------------------"""

"""-----------------------------------------------------------------------------
 * Function:    init
 * Description: Initializes global variables, setting them to be any user-
 *              supplied values if appropriate.
 * Arguments:   argv1 - number of bodies
 *              argv2 - radius of each body
 *              argv3 - number of time steps
 *              argv4 - 1 to enable output for gui, 0 otherwise
 * Returns:     Nothing.
 * --------------------------------------------------------------------------"""
def init():
    # Initialize values from command line or from module file values.
    num_bodies = SM.NUM_BODIES
    body_radius = SM.BODY_RADIUS
    timesteps = SM.TIMESTEPS
    enable_gui = SM.ENABLE_GUI

    # Open file in write mode in order to start fresh.
    with open("testie.txt", "w") as file:
        file.write("test")
        file.write(" ")

        # Write num_bodies, body_radius, & timesteps to file for GUI.
        file.write(str(num_bodies))
        file.write(" ")
        file.write(str(body_radius))
        file.write(" ")
        file.write(str(timesteps))
        file.write(" ")

    # Close the file.
    file.close()


    return


init()


