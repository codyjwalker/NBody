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


from tkinter import *

root = Tk()
root.title('N-Body Gravitational Simulation')
root.geometry("300x400")


label1 = Label(root, text = "Number of bodies:    ")
label2 = Label(root, text = "Number of timesteps:    ")

sb1 = Spinbox(root, width = 5, from_ = 1, to = 10)
sb2 = Spinbox(root, width = 5, from_ = 1, to = 3000)

cb1 = Checkbutton(root, text = "Enable Debug Print Statements")
cb2 = Checkbutton(root, text = "Enable Graphical Output")



label1.grid(row = 0, column = 0, sticky = E)
label2.grid(row = 1, column = 0, sticky = E)

sb1.grid(row = 0, column = 2, sticky = W)
sb2.grid(row = 1, column = 2, sticky = W)

cb1.grid(columnspan = 2, sticky = W)
cb2.grid(columnspan = 2, sticky = W)


"""
top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

graphics_var = IntVar()
Checkbutton(top_frame, text = 'Enable Graphical Output', variable =
            graphics_var).grid(row = 0, sticky = W)

debug_print_var = IntVar()
Checkbutton(top_frame, text = 'Enable Debug Print Statements', variable =
            debug_print_var).grid(row = 1, sticky = W)

num_bodies_label = StringVar()
num_bodies_label.set("Number of bodies:")
label_dir = Label(bottom_frame, textvariable = num_bodies_label, height = 4)
label_dir.pack(side = "left")

num_bodies = StringVar(None)
num_bodies_box = Spinbox(bottom_frame, textvariable = num_bodies, from_ = 1, to
                         = 10)
num_bodies_box.pack(side = "left")

timesteps = StringVar(None)
timesteps_box = Spinbox(bottom_frame, textvariable = timesteps, from_ = 1, to
                        = 3000)
timesteps_box.pack(side = "left")

"""


"""
bottom_frame = Scale(root, from_ = 1, to = 20, orient = HORIZONTAL)
bottom_frame.pack()
bottom_frame = Scale(root, from_ = 1, to = 3000, orient = HORIZONTAL)
bottom_frame.pack()
"""

mainloop()


""" END GUI.py """
