import tkinter as tk
from datetime import datetime
import math
import decimal

race_time = 0
counter = 0
running = False
batt = 100
count_up = False
one_lap = 0

def S2Time(secs):
    hours = (secs / (60 * 60)) % 24
    hours = math.trunc(hours)
    minutes = (secs / 60) % 60
    minutes = math.trunc(minutes)
    seconds = secs % 60
    seconds = math.trunc(seconds)
    return hours, minutes, seconds

def add_time(time_label, onelap_label, t_type, timer):
    global counter
    global race_time
    global one_lap
    if timer == 'counter':
        if t_type == 'hr':
            counter += 3600
        elif t_type == 'min':
            counter += 60
        else:
            counter += 1
    else:
        if t_type == 'hr':
            one_lap += 3600
        elif t_type == 'min':
            one_lap += 60
        else:
            one_lap += 1
    hrs, mins, secs = S2Time(counter)
    display = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(hrs, mins, secs)
    time_label['text'] = display
    hrs, mins, secs = S2Time(one_lap)
    onelap_display = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(hrs, mins, secs)
    onelap_label['text'] = onelap_display
    race_time = counter

def counter_label(time_label, batt_label):
    def count():
        global counter
        global batt
        global count_up
        global one_lap
        if running:
            if not count_up:
                hrs, mins, secs = S2Time(counter)
                display = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(hrs, mins, secs)
                time_label['text']=display   # Or label.config(text=display)
                batt = ((counter + one_lap) / (race_time + one_lap)) * 100
                batt_display = "Batt: %.2f" % (batt)
                batt_label['text'] = batt_display
                time_label.after(1000, count)
                counter -= 1
                if counter == 0:
                    count_up = True
            else:
                hrs, mins, secs = S2Time(counter)
                display = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(hrs, mins, secs)
                time_label['text']=display   # Or label.config(text=display)
                batt = ((-counter + one_lap) / (race_time + one_lap)) * 100
                batt_display = "Batt: %.2f" % (batt)
                batt_label['text'] = batt_display
                time_label.after(1000, count) 
                counter += 1
    count()     

# start function of the stopwatch
def Start(time_label, batt_label):
    global running
    running=True
    counter_label(time_label, batt_label)
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
def Reset(time_label, batt_label, onelap_label):
    global counter
    global one_lap
    global batt
    counter = 0
    one_lap = 0
    batt = 0
    # If rest is pressed after pressing stop.
    Stop()
    time_label['text'] = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(0, 0, 0)
    batt_label['text'] = "Batt: %.2f" % (batt)
    onelap_label['text'] = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(0, 0, 0)
   
root = tk.Tk()
root.title("Stopwatch")
   
# Fixing the window size.
root.minsize(width = 300, height = 100)
time_label = tk.Label(root, text = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(0, 0, 0), fg="black", font="Verdana 30 bold")
time_label.pack()
onelap_label = tk.Label(root, text = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(0, 0, 0), fg = "black", font = "Verdana 10")
onelap_label.pack()
onelapOil_label = tk.Label(root, "Oil/lap: %.2f" % (batt), fg = "black", font = "Verdana 10")
onelapOil_label.pack()
# batt_label = tk.Label(root, text = "Batt: %.2f" % (batt), fg = "black", font = "Verdana 20")
# batt_label.pack()
f = tk.Frame(root)
add_hr = tk.Button(f, text='+1hr', width=6, command=lambda:add_time(time_label, onelap_label, 'hr', 'counter'))
add_min = tk.Button(f, text='+1min', width=6, command=lambda:add_time(time_label, onelap_label, 'min', 'counter'))
add_sec = tk.Button(f, text='+1sec', width=6, command=lambda:add_time(time_label, onelap_label, 'sec', 'counter'))
add_hr_onelap = tk.Button(f, text='+1hr', width=6, command=lambda:add_time(time_label, onelap_label, 'hr', 'onelap'))
add_min_onelap = tk.Button(f, text='+1min', width=6, command=lambda:add_time(time_label, onelap_label, 'min', 'onelap'))
add_sec_onelap = tk.Button(f, text='+1sec', width=6, command=lambda:add_time(time_label, onelap_label, 'sec', 'onelap'))
start = tk.Button(f, text='Start', width=6, command=lambda:Start(time_label, batt_label))
stop = tk.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = tk.Button(f, text='Reset',width=6, state='normal', command=lambda:Reset(time_label, batt_label, onelap_label))
f.pack(anchor = 'center', pady = 5)
add_hr.grid(row = 0, column = 0)
add_min.grid(row = 0, column = 1)
add_sec.grid(row = 0, column = 2)
add_hr_onelap.grid(row = 1, column = 0)
add_min_onelap.grid(row = 1, column = 1)
add_sec_onelap.grid(row = 1, column = 2)
start.grid(row = 2, column = 0)
stop.grid(row = 2, column = 1)
reset.grid(row = 2, column = 2)
root.mainloop()