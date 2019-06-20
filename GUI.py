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
 " Updated:         17 June 2019
 "
 " --------------------------------------------------------------------------"""

pdb = 1

# TODO: FIGURE OUT WHETHER OR NOT TO MAKE THIS A CLASS FILE!!!

from tkinter import *
import subprocess


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


    with open("parameters.txt", "w") as file:
        # Write the values to file.
        file.write(str(num_bodies_sb.get()))
        file.write("\n")
        file.write(str(num_timesteps_sb.get()))
        file.write("\n")
        file.write(str(body_radius_sb.get()))
        file.write("\n")
        file.write(str(body_mass_sb.get()))
        file.write("\n")
        file.write(str(xmin_sb.get()))
        file.write("\n")
        file.write(str(ymin_sb.get()))
        file.write("\n")
        file.write(str(xmax_sb.get()))
        file.write("\n")
        file.write(str(ymax_sb.get()))
        file.write("\n")
        file.write(str(var_debug.get()))
        file.write("\n")
        file.write(str(var_graphics.get()))
        file.write("\n")

    if (pdb):
        print(num_bodies_sb.get())
        print(num_timesteps_sb.get())
        print(body_radius_sb.get())
        print(body_mass_sb.get())
        print(xmin_sb.get())
        print(ymin_sb.get())
        print(xmax_sb.get())
        print(ymax_sb.get())
        print(var_debug.get())
        print(var_graphics.get())

    # Dont forget to bring a towel!
    file.close()

    # Close out of the GUI input window.
    root.destroy()

    # Run the bash script that launches the computational program.
    subprocess.call(['./PythonVersion.sh'])
    return


# Initialize the Tkinter
root = Tk()
root.title('N-Body Gravitational Simulation')
# root.geometry("300x400")

# Default values for spinboxes.
var_num_bodies = StringVar(root)
var_num_timesteps = StringVar(root)
var_body_radius = StringVar(root)
var_body_mass = StringVar(root)
var_xmin = StringVar(root)
var_ymin = StringVar(root)
var_xmax = StringVar(root)
var_ymax = StringVar(root)
var_debug = IntVar()
var_graphics = IntVar()


var_num_bodies.set("4")
var_num_timesteps.set("300")
var_body_radius.set("5")
var_body_mass.set("10000000000")
var_xmin.set("0")
var_ymin.set("0")
var_xmax.set("1600")
var_ymax.set("900")
var_debug.set(1)
var_graphics.set(1)

# Labels for each of the Spinboxes.
num_bodies_label = Label(root, text = "Number of bodies:    ")
num_timesteps_label = Label(root, text = "Number of timesteps:    ")
body_radius_label = Label(root, text = "Radius of each body:    ")
body_mass_label = Label(root, text = "Mass of each body:    ")
xmin_label = Label(root, text = "Min x value:    ")
ymin_label = Label(root, text = "Min y value:    ")
xmax_label = Label(root, text = "Max x value:    ")
ymax_label = Label(root, text = "Max y value:    ")

# The Spinboxes for selecting values for the simulation.
num_bodies_sb = Spinbox(root, width = 12, from_ = 1, to = 10, textvariable =
                        var_num_bodies)
num_timesteps_sb = Spinbox(root, width = 12, from_ = 1, to = 3000, textvariable
                          = var_num_timesteps)
body_radius_sb = Spinbox(root, width = 12, from_ = 1, to = 50, textvariable =
                         var_body_radius)
body_mass_sb = Spinbox(root, width = 12, from_ = 100000, to = 100000000000,
                       textvariable = var_body_mass)
xmin_sb = Spinbox(root, width = 12, from_ = -3200, to = 3200, textvariable =
                  var_xmin)
ymin_sb = Spinbox(root, width = 12, from_ = -1800, to = 1800, textvariable =
                  var_ymin)
xmax_sb = Spinbox(root, width = 12, from_ = -3200, to = 3200, textvariable =
                  var_xmax)
ymax_sb = Spinbox(root, width = 12, from_ = -1800, to = 1800, textvariable =
                  var_ymax)

# Checkboxes & their respective variables.
debug_cb = Checkbutton(root, text = "Enable Debug Print Statements", variable =
                       var_debug)
graphics_cb = Checkbutton(root, text = "Enable Graphical Output", variable =
                          var_graphics)


# The button the user presses to start the simulation.
run_button = Button(root, text = "Run Simulation", width = 10, command =
                    run_simulation)

# Grid layout of all items.
# First all the labels to the left of the Spinboxes.
num_bodies_label.grid(row = 0, column = 0, sticky = E)
num_timesteps_label.grid(row = 1, column = 0, sticky = E)
body_radius_label.grid(row = 2, column = 0, sticky = E)
body_mass_label.grid(row = 3, column = 0, sticky = E)
xmin_label.grid(row = 4, column = 0, sticky = E)
ymin_label.grid(row = 5, column = 0, sticky = E)
xmax_label.grid(row = 6, column = 0, sticky = E)
ymax_label.grid(row = 7, column = 0, sticky = E)
# Then the Spinboxes themselves.
num_bodies_sb.grid(row = 0, column = 1, sticky = W)
num_timesteps_sb.grid(row = 1, column = 1, sticky = W)
body_radius_sb.grid(row = 2, column = 1, sticky = W)
body_mass_sb.grid(row = 3, column = 1, sticky = W)
xmin_sb.grid(row = 4, column = 1, sticky = W)
ymin_sb.grid(row = 5, column = 1, sticky = W)
xmax_sb.grid(row = 6, column = 1, sticky = W)
ymax_sb.grid(row = 7, column = 1, sticky = W)
# The Checkboxes.
debug_cb.grid(columnspan = 2, sticky = W)
graphics_cb.grid(columnspan = 2, sticky = W)
# The 'Run Simulation' button.
run_button.grid(columnspan = 2)


# The main loop.
mainloop()


""" END GUI.py """
