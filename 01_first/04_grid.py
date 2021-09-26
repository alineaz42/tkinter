from tkinter import*

root = Tk()
root.title("YoYo")
root.geometry("400x300")
root.iconbitmap(r"E:\DS\python\tkinter\01_first\icont.ico")
one = Label(root, text="1", font=("times new roman", 24, "bold"))
two = Label(root, text="2", font=("times new roman", 24, "bold"))
three = Label(root, text="3", font=("times new roman", 24, "bold"))
one.grid(row=0, column=0)
two.grid(row=1, column=5)
three.place(x=100, y=200)

root.mainloop()
