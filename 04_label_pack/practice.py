from tkinter import*
root = Tk()
root.title("Hello Py")
root.geometry("500x400")
base_label = Label(text="Hello Ready", font=(
    "times new roman", 15, "bold"), padx=5, pady=5, bg="gray", fg="white")
base_label.pack(side="bottom", fill="x", pady=5)

root.mainloop()
