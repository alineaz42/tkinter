from tkinter import*

root = Tk()
root.geometry("400x300")
root.title("Label and pack")
'''
text = adds text
bg= background
fg=foreground
font=sets the fonts
padx=x padding
pady=y padding
relief=border styling[SUNKEN,RAISED,GROOVE,RIDGE]
font=("times new roman", 16, "bold")
font="times new roman 16 italic"
'''
title_label = Label(text='''Lorem ipsum dolor sit amet,\n consectetur adipiscing elit. Nullam et est nec purus venenatis \ninterdum sed eget urna. Proin dignissim sollicitudin augue. \nCurabitur tincidunt a orci eget pharetra.''',
                    bg="#eba134", fg="red", padx=12, pady=22, font=("times new roman", 16, "bold"), border=3, relief=SUNKEN)
# important pack attributes
'''
anchor=nw
side=top,bottom,left,right
'''
title_label.pack(side="right", fill="x", padx=12, pady=5)


root.mainloop()
