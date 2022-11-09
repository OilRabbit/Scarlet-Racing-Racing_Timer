# Steps
# 1. Get time for one lap and oil used for one lap
# 2. Get total time
# 3. Calculate number of laps
# 4. Calculate total oil used
# 5. show oil lower limit
# 6. enable oil adding during timer

# Shows
# 1. Total oil usage
# 2. Current oil usage
# 3. Oil usage per lap
# 4. Remaining time
# 5. time per lap

# Buttons add
# 1. Add oil (per lite and per 0.1 lite)

import tkinter as tk
from datetime import datetime
import math
import decimal

race_time = 0
counter = 0
running = False
count_up = False
one_lap = 0
oil = 0
oil_p_lap = 0
num_lap = 0
total_oil = 0

def S2Time(secs):
    hours = (secs / (60 * 60)) % 24
    hours = math.trunc(hours)
    minutes = (secs / 60) % 60
    minutes = math.trunc(minutes)
    seconds = secs % 60
    seconds = math.trunc(seconds)
    return hours, minutes, seconds

def add_time(time_label, onelap_label, oil_label, totalOil_label, t_type, timer):
    global counter
    global race_time
    global one_lap
    global num_lap
    global oil
    global oil_p_lap
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
    if one_lap != 0:
        num_lap = race_time / one_lap
    total_oil = oil_p_lap * (num_lap + 1)
    oil_label['text'] = "Oil: %.2f" % (oil)
    totalOil_label['text'] = "Total Oil: %.2f" % (total_oil)

def add_oil(oil_label, onelap_label, totalOil_label, oil_amount, oil_type):
    global oil
    global oil_p_lap
    global num_lap
    global total_oil
    if oil_type == 'oil':
        if oil_amount == 'L':
            oil += 1
        else:
            oil += 0.1
    else:
        if oil_amount == 'L':
            oil_p_lap += 1
        else:
            oil_p_lap += 0.1
        
    total_oil = oil_p_lap * (num_lap + 1)
    oil_label['text'] = "Oil: %.2f" % (oil)
    onelapOil_label['text'] = "Oil/Lap: %.2f" % (oil_p_lap)
    totalOil_label['text'] = "Total Oil: %.2f" % (total_oil)

def counter_label(time_label, oil_label, totalOil_label):
    def count():
        global counter
        global oil
        global oil_p_lap
        global num_lap
        global total_oil
        global count_up
        global one_lap
        if running:
            if not count_up:
                hrs, mins, secs = S2Time(counter)
                display = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(hrs, mins, secs)
                time_label['text']=display   # Or label.config(text=display)
                
                # batt = ((counter + one_lap) / (race_time + one_lap)) * 100
                # batt_display = "Batt: %.2f" % (batt)
                # batt_label['text'] = batt_display
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
    global oil
    global oil_p_lap
    global count_up
    global race_time
    global num_lap
    

    counter = 0
    one_lap = 0
    oil = 0
    oil_p_lap = 0
    count_up = False
    race_time = 0
    num_lap = 0
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
onelap_label = tk.Label(root, text = 'Time/Lap: {0:02.0f}:{1:02.0f}:{2:02.0f}'.format(0, 0, 0), fg = "black", font = "Verdana 10")
onelap_label.pack()

oil_label = tk.Label(root, text = "Oil: %.2f" % (oil), fg = "black", font = "Verdana 10")
oil_label.pack()
onelapOil_label = tk.Label(root, text = "Oil/Lap: %.2f" % (oil_p_lap), fg = "black", font = "Verdana 10")
onelapOil_label.pack()
totalOil_label = tk.Label(root, text = "Total Oil: %.2f" % (total_oil), fg = "black", font = "Verdana 10")
totalOil_label.pack()

f = tk.Frame(root)
add_hr = tk.Button(f, text='+1hr', width=6, command=lambda:add_time(time_label, onelap_label, oil_label, totalOil_label, 'hr', 'counter'))
add_min = tk.Button(f, text='+1min', width=6, command=lambda:add_time(time_label, onelap_label, oil_label, totalOil_label, 'min', 'counter'))
add_sec = tk.Button(f, text='+1sec', width=6, command=lambda:add_time(time_label, onelap_label, oil_label, totalOil_label, 'sec', 'counter'))
add_hr_onelap = tk.Button(f, text='+1hr', width=6, command=lambda:add_time(time_label, onelap_label, oil_label, totalOil_label, 'hr', 'onelap'))
add_min_onelap = tk.Button(f, text='+1min', width=6, command=lambda:add_time(time_label, onelap_label, oil_label, totalOil_label, 'min', 'onelap'))
add_sec_onelap = tk.Button(f, text='+1sec', width=6, command=lambda:add_time(time_label, onelap_label, oil_label, totalOil_label, 'sec', 'onelap'))

addOil_lite = tk.Button(f, text='+1L', width=6, command=lambda:add_oil(oil_label, onelapOil_label, totalOil_label, 'L', 'oil'))
addOil_smalllite = tk.Button(f, text='+0.1L', width=6, command=lambda:add_oil(oil_label, onelapOil_label, totalOil_label, '0.1L', 'oil'))

addOilpl_lite = tk.Button(f, text='+1L', width=6, command=lambda:add_oil(oil_label, onelapOil_label, totalOil_label, 'L', 'onelap'))
addOilpl_smalllite = tk.Button(f, text='+0.1L', width=6, command=lambda:add_oil(oil_label, onelapOil_label, totalOil_label, '0.1L', 'onelap'))

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

addOil_lite.grid(row = 2, column = 0)
addOil_smalllite.grid(row = 2, column = 2)

addOilpl_lite.grid(row = 3, column = 0)
addOilpl_smalllite.grid(row = 3, column = 2)

start.grid(row = 4, column = 0)
stop.grid(row = 4, column = 1)
reset.grid(row = 4, column = 2)
root.mainloop()