# Python program to illustrate a stop watch
# using Tkinter
#importing the required libraries
import time
race_time = 2700
battery = 100

def countdown(total, one_lap):
    global race_time
    race_time = total * 60
    global battery
    remaining_time = total * 60
    
    while remaining_time >= 0:
        mins, secs = divmod(remaining_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        battery = ((remaining_time + one_lap) / (race_time + one_lap)) * 100
        print('Time Left: ', timer, '     Battery Lower Limit: ', round(battery, 1), end="\r")
        time.sleep(1)
        remaining_time -= 1
        
    remaining_time += 2
    
    while True:
        mins, secs = divmod(remaining_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        battery = ((-remaining_time + one_lap) / (race_time + one_lap)) * 100
        print('Time Left: ', timer, '     Battery Lower Limit: ', round(battery, 1), end="\r")
        time.sleep(1)
        remaining_time += 1


total = input('Total Race Time (in minute): ')
one_lap = input('Time for one Lap (in second): ')
print('\n')

countdown(int(total), int(one_lap))