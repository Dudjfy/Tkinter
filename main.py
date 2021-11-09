from tkinter import *

root = Tk()

# Functions
def click(x):
  print(x)

# Label
#entry = Entry(root, text="LOL")
#entry.grid(row=0, column=0)

buttons = []
for y in range(3):
  for x in range(3):
    Button(root, 
               text=str(y * 3 + x + 1), 
               padx=10, 
               pady=10, 
               command=lambda r=y * 3 + x + 1: click(r)).grid(row=4 - y, column=x)

# Show screen

root.mainloop()