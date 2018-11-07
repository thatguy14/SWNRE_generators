# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:23:40 2018

@author: Matthew
"""

import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.parent = parent
        self.button = tk.Button(self.parent, text="Npc Name Generator", 
                                command=self.create_faction_window)
        self.button.grid(row=0,column=0)

    def npc_name_generator(self):
        self.faction_win = fac.faction_gui(self.parent)
        

    

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    #main.pack(side="top", fill="both", expand=True)
    root.mainloop()