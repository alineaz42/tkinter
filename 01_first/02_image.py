########################################################
# importing modules
from tkinter import *
from PIL import Image, ImageTk
# 3
root = Tk()
# sizes
# root.geometry("400x300")
# # root.minsize(300, 200)
# # root.maxsize(1000, 800)
# ######################################################
# image = Image.open("photo.jpg")
# # photo = PhotoImage(file="1.jpg")
# photo = ImageTk.PhotoImage(image)
# ################################################
# photo_label = Label(image=photo)
# photo_label.pack()
# ###############################################
photo = PhotoImage(file="imageTwo.png")
photo_label = Label(photo)
photo_label.pack()
root.mainloop()
