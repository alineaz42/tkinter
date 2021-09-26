from tkinter import*
from madlib1 import madlib1
root = Tk()
root.geometry('300x300')
root.title("Mad Libs Games")
Label(root, text="Mad Libs Generator\n Have fun!!!",
      font=("arial", 20, "bold")).pack()
Label(root, text="Click Any One", font=("arial", 15, "bold")).place(x=40, y=80)

# buttons
Button(root, text="The Photographer", font=("arial", 15),
       command=madlib1, bg="ghost white").place(x=60, y=120)
root.mainloop()
