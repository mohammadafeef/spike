import tkinter as tk
roott = tk.Tk()
roott.geometry("1000x700")

label = tk.Label(roott, text="Enter The Password", font=('Arial',18))
label.pack(padx=30,pady=30)
roott.mainloop()