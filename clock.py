from tkinter import Frame, Label, Tk
from time import strftime

clock = Tk()
clock.title("Clock")
clock.geometry("720x480")

def now():
    lbl_time.config(text =  strftime("%I:%M:%S %p"))
    lbl_date.config(text = strftime("%D"))
    lbl_day.config(text = strftime("%a"))
    lbl_time.after(1000, now)

frame_home = Frame(clock, bg = "#111")
frame_home.place(relwidth = 1, relheight = 1, x = 0, y = 0)

lbl_time = Label(frame_home, bg = "#0A0A0A", fg = "#07F", font = ("Agency FB", 32))
lbl_time.place(relwidth = 0.5, relheight = 0.3, relx = 0.25, rely = 0.1)

lbl_date = Label(frame_home, bg = "#111", fg = "#09F", font = ("Agency FB", 24))
lbl_date.place(relwidth = 0.3, relheight = 0.1, relx = 0.35, rely = 0.42)

lbl_day = Label(frame_home, bg = "#111", fg = "#09F", font = ("Agency FB", 18))
lbl_day.place(relwidth = 0.25, relheight = 0.1, relx = 0.375, rely = 0.52)

now()

clock.mainloop()