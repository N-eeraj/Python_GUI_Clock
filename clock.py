# importing libraries & framework
from tkinter import Tk, Frame, Button, Label, Entry, messagebox
from time import sleep, strftime, struct_time
from tkinter.constants import END

# creating gui object
clock = Tk()
clock.title("Clock")
clock.geometry("720x480")

### functions
# function to update time
def updateTime():
    lbl_time.config(text =  strftime("%I:%M:%S %p"))
    lbl_date.config(text = strftime("%D"))
    lbl_day.config(text = strftime("%A"))
    frame_home.after(1000, updateTime)

# function to load timer frame
def timerFrame():
    
    # function to start timer
    def startTimer():
        minute = int(edt_minute.get())
        second = int(edt_second.get())
        if minute > 60:
            messagebox.showerror("Error", "Maximum time is 1 Hour\n60:00")
        elif minute == 60 and second != 0:
            messagebox.showerror("Error", "Maximum time is 1 Hour\n60:00")
        elif minute < 0:
            messagebox.showerror("Error", "Enter Number from 0 to 60")
        else:
            if second > 59:
                messagebox.showerror("Error", "Enter Number from 0 to 59")
            elif second < 0:
                messagebox.showerror("Error", "Enter Number from 0 to 59")
            elif second == 0:
                messagebox.showerror("Error", "Maximum time is 1 Second\n00:01")
            else:
                timer_time = minute * 60 + second
                while timer_time != 0:
                    timer_time -= 1
                    sleep(1)
                messagebox.showinfo("Time Up", "Time Up")
                edt_minute.delete(0, END)
                edt_minute.insert(0, "00")
                edt_second.delete(0, END)
                edt_second.insert(0, "00")

    # timer frame widgets
    clock.title("Timer")

    frame_timer = Frame(clock, bg = "#111")
    frame_timer.place(relwidth = 1, relheight = 1, x = 0, y = 0)

    edt_minute = Entry(frame_timer, bg = "#AAA", fg = "#003", border = 0, font = ("Agency FB", 32), justify = "center")
    edt_minute.insert(0, "00")
    edt_minute.place(relwidth = 0.2, relheight = 0.3, relx = 0.25, rely = 0.1)

    edt_second = Entry(frame_timer, bg = "#AAA", fg = "#003", border = 0, font = ("Agency FB", 32), justify = "center")
    edt_second.insert(0, "00")
    edt_second.place(relwidth = 0.2, relheight = 0.3, relx = 0.55, rely = 0.1)

    btn_start_stopwatch = Button(frame_timer, text = "Start", bg = "#3C3", fg = "#CCC", border = 0, font = ("Arial", 17), command = startTimer)
    btn_start_stopwatch.place(relwidth = 0.3, relheight = 0.125, relx = 0.35, rely = 0.5)

    btn_home = Button(frame_timer, text = "Home", bg = "#37F", fg = "#CCC", border = 0, font = ("Arial", 17), command = lambda: frame_timer.destroy())
    btn_home.place(relwidth = 0.3, relheight = 0.125, relx = 0.35, rely = 0.7)


# home frame widgets
frame_home = Frame(clock, bg = "#111")
frame_home.place(relwidth = 1, relheight = 1, x = 0, y = 0)

lbl_time = Label(frame_home, bg = "#0A0A0A", fg = "#07F", font = ("Agency FB", 32))
lbl_time.place(relwidth = 0.5, relheight = 0.3, relx = 0.25, rely = 0.1)

lbl_date = Label(frame_home, bg = "#111", fg = "#09F", font = ("Agency FB", 24))
lbl_date.place(relwidth = 0.3, relheight = 0.1, relx = 0.35, rely = 0.42)

lbl_day = Label(frame_home, bg = "#111", fg = "#09F", font = ("Agency FB", 18))
lbl_day.place(relwidth = 0.25, relheight = 0.1, relx = 0.375, rely = 0.5)

# btn_stopwatch = Button(frame_home, text = "Stopwatch", bg = "#C33", fg = "#111", border = 0, font = ("Arial", 16), command = stopWatchFrame)
# btn_stopwatch.place(relwidth = 0.2, relheight = 0.1, relx = 0.1, rely = 0.75)

# btn_alarm = Button(frame_home, text = "Alarm", bg = "#33C", fg = "#111", border = 0, font = ("Arial", 17), command = alarmFrame)
# btn_alarm.place(relwidth = 0.2, relheight = 0.1, relx = 0.4, rely = 0.75)

btn_timer = Button(frame_home, text = "Timer", bg = "#37F", fg = "#111", border = 0, font = ("Arial", 17), command = timerFrame)
btn_timer.place(relwidth = 0.2, relheight = 0.1, relx = 0.4, rely = 0.75)

# looping gui & updating time
updateTime()
clock.mainloop()