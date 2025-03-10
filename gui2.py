import tkinter as tk
from PIL import Image, ImageTk  

def showframe(frame):
    frame.tkraise()  
    if frame == frame2:  
        startcountdown(10) 

def fadetext():                          #fade in & out(warning)
    global alpha, fadein

    if fadein:
        alpha += 0.05  
        if alpha >= 1:
            fadein = False  
    else:
        alpha -= 0.05  
        if alpha <= 0:
            fadein = True  

    redvalue = int(255 * alpha)
    fadedcolor = f"#{redvalue:02x}0000"  
    labeltext.config(fg=fadedcolor)
    root.after(50, fadetext)  

def startcountdown(count):        # timer
    if count >= 0:
        countdownlabel.config(text=f"{count}") 
        root.after(1000, startcountdown, count - 1)  


root = tk.Tk()
root.title("boom")
root.attributes("-fullscreen", True)  
root.configure(bg="black")  

container = tk.Frame(root)                    
container.pack(fill="both", expand=True)


frame1 = tk.Frame(container, bg="black")      #1st frame
frame1.place(relwidth=1, relheight=1) 

image = Image.open("/home/stalon/Pictures/—Pngtree—caution sign signal_6015188.png")
image = image.resize((600, 600))   
photo = ImageTk.PhotoImage(image)
labelimage = tk.Label(frame1, image=photo, bg="black")  
labelimage.pack()

labeltext = tk.Label(frame1, text="WARNING!", font=("Arial", 35, "bold"), fg="black", bg="black")
labeltext.pack()

nextbutton = tk.Button(frame1, text="Next", font=("Arial", 15, "bold"), command=lambda: showframe(frame2))
nextbutton.pack(pady=10)


frame2 = tk.Frame(container, bg="black")         #2nd frame
frame2.place(relwidth=1, relheight=1)  

countdownlabel = tk.Label(frame2, text="10", font=("Arial", 200, "bold"), fg="white", bg="black")
countdownlabel.pack(expand=True)

alpha = 0  
fadein = True 

fadetext()
showframe(frame1)        #show farme1
                              
root.mainloop()

