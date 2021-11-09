from functools import partial
from tkinter import *

root = Tk()


b_size_x, b_size_y = 20, 20

# Label
entry1 = Entry(root, width=40)
entry1.grid(row=0, column=0, columnspan=4)


# Functions
def num_click(entry, num):
    entry.insert(len(entry.get()), num)


# Numbered buttons
for y in range(3):
    for x in range(3):
        num = y * 3 + x + 1
        Button(root,
               text=str(num),
               padx=b_size_x,
               pady=b_size_y,
               command=partial(num_click, entry1, num)).grid(row=4 - y, column=x)


class ButtonValues:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c


other_buttons = {
    "0": ButtonValues(1, 5, partial(num_click, entry1, 0))
}

for sign, values in other_buttons.items():
    Button(root,
           text=sign,
           padx=b_size_x,
           pady=b_size_y,
           command=values.c).grid(row=values.y, column=values.x)

# Show screen
root.mainloop()
