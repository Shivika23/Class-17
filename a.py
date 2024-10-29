from tkinter import *
root = Tk()

root.title("Sample project")
#root.geometry("300X300")
a = Label(text = "Hello world", fg = "black", bg = "green")
b = Button(text = "Click me", bg = "green", fg = "black")
e = Entry(fg = "green", bg = "black", width= 70 )
a.pack()
b.pack()
e.pack()

frame = Frame(master= root, relief= RAISED, borderwidth= 5 )
frame.pack()

t = Text(bg = "black", fg= "green")
t.pack()

root.mainloop()