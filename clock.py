from tkinter import Button, Frame, Label, Tk
from time import strftime, time

clock = Tk()
clock.title("Clock")
clock.geometry("720x480")

def updateTime():
    lbl_time.config(text =  strftime("%I:%M:%S %p"))
    lbl_date.config(text = strftime("%D"))
    lbl_day.config(text = strftime("%A"))
    frame_home.after(1000, updateTime)

def stopWatchFrame():
    pass

def alarmFrame():
    pass

def timerFrame():
    pass

frame_home = Frame(clock, bg = "#111")
frame_home.place(relwidth = 1, relheight = 1, x = 0, y = 0)

lbl_time = Label(frame_home, bg = "#0A0A0A", fg = "#07F", font = ("Agency FB", 32))
lbl_time.place(relwidth = 0.5, relheight = 0.3, relx = 0.25, rely = 0.1)

lbl_date = Label(frame_home, bg = "#111", fg = "#09F", font = ("Agency FB", 24))
lbl_date.place(relwidth = 0.3, relheight = 0.1, relx = 0.35, rely = 0.42)

lbl_day = Label(frame_home, bg = "#111", fg = "#09F", font = ("Agency FB", 18))
lbl_day.place(relwidth = 0.25, relheight = 0.1, relx = 0.375, rely = 0.5)

btn_stopwatch = Button(frame_home, text = "Stopwatch", bg = "#C33", fg = "#111", border = 0, font = ("Arial", 16), command = stopWatchFrame)
btn_stopwatch.place(relwidth = 0.2, relheight = 0.1, relx = 0.1, rely = 0.75)

btn_alarm = Button(frame_home, text = "Alarm", bg = "#33C", fg = "#111", border = 0, font = ("Arial", 17), command = alarmFrame)
btn_alarm.place(relwidth = 0.2, relheight = 0.1, relx = 0.4, rely = 0.75)

btn_timer = Button(frame_home, text = "Timer", bg = "#3C3", fg = "#111", border = 0, font = ("Arial", 17), command = timerFrame)
btn_timer.place(relwidth = 0.2, relheight = 0.1, relx = 0.7, rely = 0.75)


updateTime()

clock.mainloop()