from functools import partial
from tkinter import *

root = Tk()


# Label
entry1 = Entry(root, width=26)
entry1.grid(row=0, column=0, columnspan=3)


# Functions
def num_click(entry, num):
    entry.insert(len(entry.get()), num)


for y in range(3):
    for x in range(3):
        num = y * 3 + x + 1
        Button(root,
               text=str(num),
               padx=20,
               pady=20,
               command=partial(num_click, entry1, num)).grid(row=4 - y, column=x)

# Show screen

root.mainloop()
