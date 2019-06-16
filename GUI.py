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


from tkinter import *



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
        file.write(str(var_debug_cb.get()))
        file.write("\n")
        file.write(str(var_graphics_cb.get()))
        file.write("\n")

    # Dont forget to bring a towel!
    file.close()

    print(num_bodies_sb.get())
    print(num_timesteps_sb.get())
    print(var_debug_cb.get())
    print(var_graphics_cb.get())
    return



root = Tk()
root.title('N-Body Gravitational Simulation')
# root.geometry("300x400")


num_bodies_label = Label(root, text = "Number of bodies:    ")
num_timesteps_label = Label(root, text = "Number of timesteps:    ")

num_bodies_sb = Spinbox(root, width = 5, from_ = 1, to = 10)
num_timesteps_sb = Spinbox(root, width = 5, from_ = 1, to = 3000)

var_debug_cb = IntVar()
var_graphics_cb = IntVar()
debug_cb = Checkbutton(root, text = "Enable Debug Print Statements", variable =
                       var_debug_cb)
graphics_cb = Checkbutton(root, text = "Enable Graphical Output", variable =
                          var_graphics_cb)


run_button = Button(root, text = "Run Simulation", width = 10, command =
                    run_simulation)



num_bodies_label.grid(row = 0, column = 0, sticky = E)
num_timesteps_label.grid(row = 1, column = 0, sticky = E)

num_bodies_sb.grid(row = 0, column = 1, sticky = W)
num_timesteps_sb.grid(row = 1, column = 1, sticky = W)

debug_cb.grid(columnspan = 2, sticky = W)
graphics_cb.grid(columnspan = 2, sticky = W)

run_button.grid(columnspan = 2)




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
