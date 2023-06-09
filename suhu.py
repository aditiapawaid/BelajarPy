from tkinter import *
from tkinter import ttk

c2f = Tk()
c2f.title("Celsius to Reamur")

def convert(*args):
    try:
        value = float(celsius.get())
        reamur.set(4 / 5 * value )
    except ValueError:
        pass

mainframe = ttk.Frame(c2f, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

celsius = StringVar()
reamur = StringVar()
 
celsius_input = ttk.Entry(mainframe, width=7, textvariable=celsius)
celsius_input.grid(column=2, row=1, sticky=(W,E))
 
ttk.Label(mainframe, textvariable=reamur).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="convert", command=convert).grid(column=3, row=3, sticky=(W))

ttk.Label(mainframe, text="celsius").grid(column=3, row=1, sticky=(W))
ttk.Label(mainframe, text="reamur").grid(column=3, row=2, sticky=(W))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
celsius_input.focus()
c2f.bind('<Return>', convert)

c2f.mainloop()