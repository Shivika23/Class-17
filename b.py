from tkinter import *
root = Tk()

for i in range(3):
    for j in range(3):
        frame = Frame(master=root, relief=RAISED, borderwidth=1)
        frame.grid(row = i, column = j, padx = 5, pady = 5)
        label = Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

root.mainloop()
