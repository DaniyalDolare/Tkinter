from tkinter import *
root = Tk()
#r=IntVar()
#r.set("2")
Modes = [("Pepperoni","Pepperoni"),("Onion","Onion"),("Cheese","Cheese"),("mashroom","mashroom")]
pizza = StringVar()
pizza.set("Pepperoni")
for text,mode in Modes:
    Radiobutton(root,text=text,variable=pizza, value=mode).pack(anchor=W)
def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()
#Radiobutton(root, text="option 1", variable=r, value=1, command=lambda :
#           clicked(r.get())).pack()
#Radiobutton(root, text="option 2", variable=r, value=2, command=lambda :
#            clicked(r.get())).pack()
#my_label = Label(root,text=pizza.get())
#my_label.pack()
b = Button(root, text="click_me", command=lambda :
            clicked(pizza.get())).pack()
root.mainloop()