import tkinter as tk
from tkinter import messagebox
from gpiozero import Button, LED
import time
from threading import Thread

# GPIO setup
inputPins = [2, 3, 4, 17, 27, 22]
outputPins = [10, 9, 11, 5, 6, 13]

brownIN = Button(2)
redIN = Button(3)
orangeIN = Button(4)
yellowIN = Button(17)
greenIN = Button(27)
blueIN = Button(22)

active = [brownIN, redIN, orangeIN, yellowIN, greenIN, blueIN]
seq = [brownIN, redIN, orangeIN, yellowIN, greenIN, blueIN]

brownOUT = LED(10)
redOUT = LED(9)
orangeOUT = LED(11)
yellowOUT = LED(5)
greenOUT = LED(6)
blueOUT = LED(13)

brownOUT.off()
redOUT.off()
orangeOUT.off()
yellowOUT.off()
greenOUT.off()
blueOUT.off()

ansStr = "#41235"
preStr = "#"

# Tkinter GUI setup
root = tk.Tk()
root.title("Bomb Defusal")
root.attributes("-fullscreen", True)  # Fullscreen mode
root.configure(bg="black")

# Blinking "Activated" text
activated_label = tk.Label(
    root,
    text="Activated",
    font=("Arial", 40, "bold"),
    fg="red",
    bg="black"
)
activated_label.pack(pady=20)

# Timer countdown
timer_label = tk.Label(
    root,
    text="10:00",
    font=("Arial", 50, "bold"),
    fg="white",
    bg="black"
)
timer_label.pack(pady=50)

# Password input field (visible)
password_var = tk.StringVar()
password_entry = tk.Entry(
    root,
    textvariable=password_var,
    font=("Arial", 20)
)
password_entry.pack(pady=20)

# Submit button
submit_button = tk.Button(
    root,
    text="Submit",
    font=("Arial", 20),
    command=lambda: check_password(password_var.get())
)
submit_button.pack(pady=10)

# Bomb exploded or defused screens
exploded_label = tk.Label(
    root,
    text="Bomb Exploded!",
    font=("Arial", 60, "bold"),
    fg="white",
    bg="red"
)

defused_label = tk.Label(
    root,
    text="Bomb Defused!",
    font=("Arial", 60, "bold"),
    fg="white",
    bg="green"
)

# Function to blink the "Activated" text
def blink_activated():
    while True:
        activated_label.config(fg="red" if activated_label.cget("fg") == "black" else "black")
        time.sleep(0.5)

# Function to update the timer
def update_timer():
    remaining_time = 1200  # 10 minutes in seconds
    while remaining_time > 0:
        minutes, seconds = divmod(remaining_time, 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        time.sleep(1)
        remaining_time -= 1
        if remaining_time <= 0:
            show_exploded_screen()
            break

# Function to check the password
def check_password(password):
    if password == "NRTPU10":  # Replace with your actual password
        # Show alert message to start cutting wires
        messagebox.showinfo("Correct Password", "Password correct! Start cutting the wires.")
        # Start wire-cutting in a separate thread
        wire_thread = Thread(target=start_wire_cutting, daemon=True)
        wire_thread.start()
    else:
        show_exploded_screen()

# Function to show the exploded screen
def show_exploded_screen():
    hide_all_widgets()
    exploded_label.pack(fill="both", expand=True)

# Function to show the defused screen
def show_defused_screen():
    hide_all_widgets()
    defused_label.pack(fill="both", expand=True)

# Function to hide all widgets
def hide_all_widgets():
    for widget in root.winfo_children():
        widget.pack_forget()

# Function to start the wire-cutting process
def start_wire_cutting():
    global preStr
    while True:
        for i in active:
            if not i.is_pressed:
                preStr += str(seq.index(i))
                active.remove(i)
            if preStr in ansStr:
                print("safe")
            else:
                show_exploded_screen()
                return
            if ansStr == preStr:
                show_defused_screen()
                return

# Start the blinking and timer threads
Thread(target=blink_activated, daemon=True).start()
Thread(target=update_timer, daemon=True).start()

# Run the Tkinter main loop
root.mainloop()
