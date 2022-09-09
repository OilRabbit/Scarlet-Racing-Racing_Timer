import tkinter as tk
from datetime import datetime
import math

counter = 0
running = False
batt = 0

def S2Time(secs):
    hours = (secs / (60 * 60)) % 24
    hours = math.trunc(hours)
    minutes = (secs / 60) % 60
    minutes = math.trunc(minutes)
    seconds = secs % 60
    seconds = math.trunc(seconds)
    return hours, minutes, seconds

def add_time(time_label, t_type):
    global counter
    if t_type == 'hr':
        counter += 3600
        counter += 60
    else:
        counter += 1
    hrs, mins, secs = S2Time(counter)
    display = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(hrs, mins, secs)
    time_label['text'] = display

def counter_label(time_label):
    def count():
        if running:
            global counter
            hrs, mins, secs = S2Time(counter)
            display = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(hrs, mins, secs)
            time_label['text']=display   # Or label.config(text=display)
            time_label.after(1000, count) 
            counter -= 1
    # Triggering the start of the counter.
    count()     

# start function of the stopwatch
def Start(time_label):
    global running
    running=True
    counter_label(time_label)
    add_hr['state']='disabled'
    add_min['state']='disabled'
    add_sec['state']='disabled'
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
   
# Stop function of the stopwatch
def Stop():
    global running
    add_hr['state']='normal'
    add_min['state']='normal'
    add_sec['state']='normal'
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
   
# Reset function of the stopwatch
def Reset(time_label):
    global counter
    counter = 0
    # If rest is pressed after pressing stop.
    Stop()
    hrs, mins, secs = S2Time(counter)
    display = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(hrs, mins, secs)
    time_label['text'] = display
   
root = tk.Tk()
root.title("Stopwatch")
   
# Fixing the window size.
root.minsize(width = 300, height = 100)
time_label = tk.Label(root, text = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(0, 0, 0), fg="black", font="Verdana 30 bold")
time_label.pack()
batt_label = tk.Label(root, text = "Batt: %d" % (batt), fg = "black", font = "Verdana 20")
batt_label.pack()
f = tk.Frame(root)
add_hr = tk.Button(f, text='+1hr', width=6, command=lambda:add_time(time_label, 'hr'))
add_min = tk.Button(f, text='+1min', width=6, command=lambda:add_time(time_label, 'min'))
add_sec = tk.Button(f, text='+1sec', width=6, command=lambda:add_time(time_label, 'sec'))
start = tk.Button(f, text='Start', width=6, command=lambda:Start(time_label))
stop = tk.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = tk.Button(f, text='Reset',width=6, state='normal', command=lambda:Reset(time_label))
f.pack(anchor = 'center', pady = 5)
add_hr.grid(row = 0, column = 0)
add_min.grid(row = 0, column = 1)
add_sec.grid(row = 0, column = 2)
start.grid(row = 1, column = 0)
stop.grid(row = 1, column = 1)
reset.grid(row = 1, column = 2)
root.mainloop()


# #Import the required Libraries
# from tkinter import *
# from tkinter import ttk

# #Create an instance of Tkinter frame
# win= Tk()

# #Set the geometry of Tkinter frame
# win.geometry("750x250")

# def display_text():
#    global entry
#    string= entry.get()
#    label.configure(text=string)

# #Initialize a Label to display the User Input
# label=Label(win, text="", font=("Courier 22 bold"))
# label.pack()

# #Create an Entry widget to accept User Input
# entry= Entry(win, width= 40)
# entry.focus_set()
# entry.pack()

# #Create a Button to validate Entry Widget
# ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

# win.mainloop()




# import time
# race_time = 2700
# battery = 100

# def countdown(total, one_lap):
#     global race_time
#     race_time = total * 60
#     global battery
#     remaining_time = total * 60
    
#     while remaining_time >= 0:
#         mins, secs = divmod(remaining_time, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         battery = ((remaining_time + one_lap) / (race_time + one_lap)) * 100
#         print('Time Left: ', timer, '     Battery Lower Limit: ', round(battery, 1), end="\r")
#         time.sleep(1)
#         remaining_time -= 1
        
#     remaining_time += 2
    
#     while True:
#         mins, secs = divmod(remaining_time, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         battery = ((-remaining_time + one_lap) / (race_time + one_lap)) * 100
#         print('Time Left: ', timer, '     Battery Lower Limit: ', round(battery, 1), end="\r")
#         time.sleep(1)
#         remaining_time += 1


# total = input('Total Race Time (in minute): ')
# one_lap = input('Time for one Lap (in second): ')
# print('\n')

# countdown(int(total), int(one_lap))