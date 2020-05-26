from tkinter import *
from  tkinter import messagebox
root = Tk()
#showinfo, showwarning, showerror, askquestion, askyesno, askokcancel
def pop_up():
    response4 = messagebox.showinfo("This is my popup!", "show information!!")
    Label(root, text=response4).pack()

    response = messagebox.askyesno("This is my popup!","enter yes or no!!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes!!").pack()
    else:
        Label(root, text="You clicked no!!").pack()

    response2 = messagebox.askokcancel("This is my popup!", "enter ok or cancel!!")
    Label(root, text=response2).pack()
    if response2 == 1:
        Label(root, text="You clicked ok!!").pack()
    else:
        Label(root, text="You clicked cancel!!").pack()

    response3 = messagebox.askquestion("This is my popup!", "Do you want to ask a question!!")
    Label(root, text=response3).pack()
    if response3 == "yes":
        Label(root, text="You clicked yes!!").pack()
    else:
        Label(root, text="You clicked no!!").pack()

    response5 = messagebox.showerror("This is my popup!", "show error!!")
    Label(root, text=response5).pack()
    response6 = messagebox.showwarning("This is my popup!", "show warning!!")
    Label(root, text=response6).pack()
Button(root, text="showinfo", command=pop_up).pack()
Button(root, text="showerror", command=pop_up).pack()
Button(root, text="showwarning", command=pop_up).pack()
Button(root, text="askquestion", command=pop_up).pack()
Button(root, text="askokcancel", command=pop_up).pack()
Button(root, text="askyesno", command=pop_up).pack()
root.mainloop()