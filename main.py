from functools import partial
from tkinter import *

root = Tk()


b_size_x, b_size_y = 6, 3

# Label
entry1 = Entry(root, width=34)
# entry1.config(font=("Comic sans", 12))
entry1.grid(row=0, column=0, columnspan=4, ipady=10)


# Functions
def num_click(entry, num):
    entry.insert(len(entry.get()), num)


def equal(entry):
    length = len(entry.get())
    result = eval(entry.get())
    entry.delete(0, length)
    entry.insert(0, result)


# Numbered buttons
for y in range(3):
    for x in range(3):
        num = y * 3 + x + 1
        Button(root,
               text=str(num),
               width=b_size_x,
               height=b_size_y,
               command=partial(num_click, entry1, num)).grid(row=4 - y, column=x)


class ButtonValues:
    def __init__(self, x, y, c, w=b_size_x, h=b_size_y):
        self.x = x
        self.y = y
        self.c = c
        self.w = w
        self.h = h


other_buttons = {
    "0": ButtonValues(1, 5, partial(num_click, entry1, 0)),
    ".": ButtonValues(2, 5, partial(num_click, entry1, ".")),
    "=": ButtonValues(3, 5, partial(equal, entry1)),
}

for sign, values in other_buttons.items():
    Button(root,
           text=sign,
           width=values.w,
           height=values.h,
           command=values.c).grid(row=values.y, column=values.x)

# Show screen
root.mainloop()
