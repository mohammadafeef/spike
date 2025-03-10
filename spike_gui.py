"""from tkinter import *

window = Tk()
window.attributes('-fullscreen',True)

photo = PhotoImage(file='pngwing.png')
label = Label(window, text="Inactive", font=('Arial', 50, 'bold') ,pady=80,image=photo, compound=TOP)
label.pack()

window.mainloop()
"""

from tkinter import *
import itertools

def fade_text():
    global fade_index
    fade_index = (fade_index + 1) % len(fade_values)
    color = f"#000000{fade_values[fade_index]:02x}"
    label.config(fg=color)
    window.after(100, fade_text)

def blink_text():
    global blink_state
    blink_state = not blink_state
    label.config(fg="black" if blink_state else "white")
    window.after(500, blink_text)

window = Tk()
window.attributes('-fullscreen', True)

photo = PhotoImage(file='pngwing.png')
label = Label(window, text="Inactive", font=('Arial', 50, 'bold'), pady=80, image=photo, compound=TOP)
label.pack()

# Fade effect setup
fade_values = list(itertools.chain(range(0, 256, 25), range(255, -1, -25)))
fade_index = 0

# Blink effect setup
blink_state = True

# Call only one effect at a time
#fade_text()  # Uncomment for fade effect
blink_text()  # Uncomment for blink effect

window.mainloop()
