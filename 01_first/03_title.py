from tkinter import*

root = Tk()
root.title("First GUI")
root.geometry("300x300+0+0")
root.iconbitmap(r"E:\DS\python\tkinter\01_first\icont.ico")
# labels
name = Label(root, text="Ali Neaz", font=("times new roman", 35, "italic"))
# name.pack(side=TOP)
# name.pack(side=LEFT)
# name.pack(side=RIGHT)
name.pack(side=BOTTOM)
root.mainloop()
