from tkinter import *
from PIL import ImageTk, Image
root = Tk()
my_img1 = ImageTk.PhotoImage(Image.open('IMAGES\download.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('IMAGES\download (1).jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('IMAGES\download (2).jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('IMAGES\download (3).jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('IMAGES\download (4).jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('IMAGES\download (5).jpg'))
my_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]
status = Label(root,text="image 1 of "+str(len(my_list)), bd=1, relief=SUNKEN, anchor=E)
my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)
def forward_back(num):
    global my_label
    global button_fwd
    global button_back
    my_label.grid_forget()
    my_label = Label(image=my_list[num-1])
    button_fwd = Button(root, text=">>", command=lambda: forward_back(num+1))
    button_back = Button(root, text="<<", command=lambda: forward_back(num-1))
    if num==6:
        button_fwd = Button(root, text=">>", state=DISABLED)
    if num==1:
        button_back = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_fwd.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text="image "+ str(num) +" of " + str(len(my_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
button_back = Button(root,text="<<", command = lambda : forward_back(1))
button_exit = Button(root,text="EXIT",command=root.quit)
button_fwd = Button(root, text=">>",command = lambda : forward_back(2))
button_exit.grid(row=1,column=1)
button_fwd.grid(row=1,column=2)
button_back.grid(row=1, column=0)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
root.mainloop()
