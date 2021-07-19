from tkinter import Frame, Label, Tk
from time import strftime

clock = Tk()
clock.title("Clock")
clock.geometry("720x480")

def now():
    lbl_time.config(text =  strftime("%I:%M:%S %p"))
    lbl_time.after(1000, now)
    date = strftime("%D")
    day = strftime("%a")

frame_home = Frame(clock, bg = "#111")
frame_home.place(relwidth = 1, relheight = 1, x = 0, y = 0)

lbl_time = Label(frame_home, bg = "#000", fg = "#07F", font = ("Agency FB", 32))
lbl_time.place(relwidth = 0.5, relheight = 0.3, relx = 0.25, rely = 0.1)

now()

clock.mainloop()