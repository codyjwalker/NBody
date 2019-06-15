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


w = Tk()
w.title('N-Body Gravitational Simulation')
button = Button(w, text='Click Me!!!', width=20, command=w.destroy)
button.pack()
w.mainloop()


""" END GUI.py """
