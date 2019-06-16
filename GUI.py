"""-----------------------------------------------------------------------------
 "
 " File:            GUI.py
 " Author:          Cody Walker
 " Project:         Parallel Project 1 - n-Bodies and Collisions
 " Description:     A GUI for the N-Body Gravitational simulation.  Allows the
 "                  user to enter values such as body mass, body radius, etc.
 "                  into a dialogue menu to be used for the simulation.
 "                  languages.
 " Created:         15 June 2019
 " Updated:         15 June 2019
 "
 " --------------------------------------------------------------------------"""

# TODO
"""
TO BE USED FOR CALLING BASH SCRIPT TO RUN PROGRAM:
    import subprocess
    subprocess.call(['./test.sh'])
WHERE test.sh IS A SIMPLE SHELL SCRIPT
"""


pdb = 1


from tkinter import *


"""-----------------------------------------------------------------------------
 " Function:    run_simulation
 " Description: Invoked upon the user pressing the 'Run Simulatin' button.
 "              First writes all the values to a file so that the computational
 "              programs can access them, then runs a bash script to run the
 "              appropriate program(s) in order to run the simulation.
 " Arguments:   None.
 " Returns:     Nothing.
 " --------------------------------------------------------------------------"""
def run_simulation():
    global num_bodies_sb
    global num_timesteps_sb
    global var_debug_cb
    global var_graphics_cb


    with open("testie.txt", "w") as file:
        # Write the values to file.
        file.write(str(num_bodies_sb.get()))
        file.write("\n")
        file.write(str(num_timesteps_sb.get()))
        file.write("\n")
        file.write(str(body_radius_sb.get()))
        file.write("\n")
        file.write(str(body_mass_sb.get()))
        file.write("\n")
        file.write(str(var_debug_cb.get()))
        file.write("\n")
        file.write(str(var_graphics_cb.get()))
        file.write("\n")

    if (pdb):
        print(num_bodies_sb.get())
        print(num_timesteps_sb.get())
        print(body_radius_sb.get())
        print(body_mass_sb.get())
        print(var_debug_cb.get())
        print(var_graphics_cb.get())

    # Dont forget to bring a towel!
    file.close()
    return



root = Tk()
root.title('N-Body Gravitational Simulation')
# root.geometry("300x400")


# Labels for each of the Spinboxes.
num_bodies_label = Label(root, text = "Number of bodies:    ")
num_timesteps_label = Label(root, text = "Number of timesteps:    ")
body_radius_label = Label(root, text = "Radius of each body:    ")
body_mass_label = Label(root, text = "Mass of each body:    ")

# The Spinboxes for selecting values for the simulation.
num_bodies_sb = Spinbox(root, width = 12, from_ = 1, to = 10)
num_timesteps_sb = Spinbox(root, width = 12, from_ = 1, to = 3000)
body_radius_sb = Spinbox(root, width = 12, from_ = 1, to = 50)
body_mass_sb = Spinbox(root, width = 12, from_ = 100000, to = 10000000000)

# Checkboxes & their respective variables.
var_debug_cb = IntVar()
var_graphics_cb = IntVar()
debug_cb = Checkbutton(root, text = "Enable Debug Print Statements", variable =
                       var_debug_cb)
graphics_cb = Checkbutton(root, text = "Enable Graphical Output", variable =
                          var_graphics_cb)


# The button the user presses to start the simulation.
run_button = Button(root, text = "Run Simulation", width = 10, command =
                    run_simulation)

# Grid layout of all items.
num_bodies_label.grid(row = 0, column = 0, sticky = E)
num_timesteps_label.grid(row = 1, column = 0, sticky = E)
body_radius_label.grid(row = 2, column = 0, sticky = E)
body_mass_label.grid(row = 3, column = 0, sticky = E)

num_bodies_sb.grid(row = 0, column = 1, sticky = W)
num_timesteps_sb.grid(row = 1, column = 1, sticky = W)
body_radius_sb.grid(row = 2, column = 1, sticky = W)
body_mass_sb.grid(row = 3, column = 1, sticky = W)

debug_cb.grid(columnspan = 2, sticky = W)
graphics_cb.grid(columnspan = 2, sticky = W)

run_button.grid(columnspan = 2)


# The main loop.
mainloop()


""" END GUI.py """
