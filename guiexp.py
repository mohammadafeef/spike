import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("code checker")

root.geometry("1000x700")



actuall= "something u put"

def evaluvation():
     enteredcode= a.get()
     if enteredcode ==actuall:
        messagebox.showinfo("Result", "Correct code")
     else:
        messagebox.showerror("Result", "Incorrect code")

def clear():
    a.delete(0, tk.END)
    a.insert(0, "Enter the code")
    a.config(fg= 'grey')


def presss(event):
     if a.get() == "Enter the code":
         a.delete(0, tk.END)
         a.config(fg= 'black')

def presss1(event):
     if not a.get():
        a.insert(0, "Enter the code")
        a.config(fg = 'grey')


label = tk.Label(root, text="Enter the code")
label.pack(pady=10)

a = tk.Entry(root, fg = 'grey')
a.insert(0, "Enter the code")
a.bind("<KeyPress>",  presss)
a.bind("<FocusOut>", presss1)
a.pack(pady=10)

checkbtn = tk.Button(root, text = "CHECK", command=evaluvation)
checkbtn.pack(pady = 10)

clearbtn = tk.Button(root, text ="CLEAR",  command=clear)
clearbtn.pack(pady = 10)

root.mainloop()

