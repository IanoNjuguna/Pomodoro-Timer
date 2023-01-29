#!/bin/python3
import time
import os
from tkinter import *
from tkinter import messagebox

# Create interface object
timerWindow = Tk()
timerWindow.geometry("600x300")
timerWindow.title("Pomodoro Timer by Iano")
timerWindow.configure(background = 'black')

# Set variables for the three strings used to keep track of time
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()

# Set strings to default value
hourString.set("00")
minuteString.set("00")
secondString.set("00")

# Request for user input
hourTextbox = Entry(timerWindow, width=3, font=("calibri", 20, ""), textvariable=hourString)
minuteTextbox = Entry(timerWindow, width=3, font=("calibri", 20, ""), textvariable=minuteString)
secondTextbox = Entry(timerWindow, width=3, font=("calibri", 20, ""), textvariable=secondString)

# Center textboxes
hourTextbox.place(x=170, y=180)
minuteTextbox.place(x=220, y=180)
secondTextbox.place(x=270, y=180)

# Running the timer
def runTimer():
    try:
        clockTime = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())
    except:
        print("Incorrect values")

    while (clockTime > -1):

        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if (totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)

        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))

# Update interface
        timerWindow.update()
        time.sleep(1)

# Inform user time has elapsed
        if (clockTime) == 0:
            os.system('spd-say "Time is up!"')
            messagebox.showinfo("", "Your time has elapsed")

        clockTime -= 1

# Set Button(s)
setTimeButton = Button(timerWindow, text='Set Time', bd='5', command=runTimer)
setTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER)

# Keep looping
timerWindow.mainloop()

