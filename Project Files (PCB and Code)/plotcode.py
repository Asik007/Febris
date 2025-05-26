from matplotlib import *
from matplotlib import style
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import csv
import numpy as np
import random
import serial

import tkinter as tk
import tkinter.ttk as ttk



#from itertools import count
# ser.timeout = 10 #specify timeout when using readline()
# ser.open()
# if ser.is_open==True:
# plt.style.use('fivethirtyeight')



# GPIO.setmode(GPIO.BCM)

#interface stuff


root = tk.Tk()
#
# def Cel():
#     ser.flushInput()
#     ser.write('ce')
#     pass
#
# def Fahren():
#     ser.flushInput()
#     ser.write('f')
#     pass
#
# def BPM_go_func():
#     ser.flushInput()
#     ser.write('b')
#     pass
#
# def BPM_st_func():
#     ser.write('bst')
#     pass
#
# def ECG_go_func():
#     ser.flushInput()
#     ser.write('c')
#     pass
#
# def ECG_st_func():
#     ser.write('est')
#     pass
#
# def data_exp():
#     #pop up window of the root directory path of csv
#     path = (os.showcwd()+"/Data")
#     showinfo('Directory to Data', 'path')
#     pass
#
# def TMP_decode(ser_text):
#     TMP_val = ser_text
#     with open('raw_data.csv', 'a', newline='') as f_object:
#         field_names = ['Time','Temp']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#         writer.writeheader()
#         writer.writerow({'Time': time.time.ct, 'Temp': TMP_val})
#     pass
#
# def ECG_decode(ser_text):
#     ser_text = HR_val
#     with open('raw_data.csv', 'a') as f_object:
#         field_names = ['Time','HR']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#         writer.writeheader()
#         writer.writerow({'Time': time.time.ct, 'HR': HR_val})
#     pass
#
# def BPM_decode(str):
#     listRes = [(list(string.split(', ')))]
#     with open('raw_data.csv', 'a') as f_object:
#         field_names = ['Time','S', 'D']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#         writer.writeheader()
#         writer.writerow({'Time': time.time.ct, 'S': 'insety systolic', 'D': 'insert d'})
#     pass
#
# def Temp_int():
#     ser.flushInput()
#     ser.write("a")
#     pass
#
#

# build ui
frame1 = tk.Frame(root)
temp = tk.Label(frame1)
unit = tk.StringVar(value='Temperature (F)')
temp.configure(activeforeground='#ffffff', background='#505351', font='{clean} 14 {}', foreground='#fff')
temp.configure(relief='flat', takefocus=True, text='Temperature (F)', textvariable=unit)
temp.place(anchor='nw', relx='0.0', x='0', y='0')
Start = tk.Button(frame1)
Start.configure(height='1', text='Start', width='5')
Start.place(anchor='nw', rely='0.1', x='0', y='0')
# Start.configure(command=Temp_int)
Celcius = tk.Button(frame1)
Celcius.configure(height='1', text='Celcius', width='5')
Celcius.place(anchor='nw', rely='0.18', x='0', y='0')
# Celcius.configure(command=Cel)
fah = tk.Button(frame1)
fah.configure(height='1', text='Fahernheit', width='7')
fah.place(anchor='nw', rely='0.26', x='0', y='0')
# fah.configure(command=Fahren)
TMP_text = tk.Label(frame1)
TMP = tk.StringVar(value='97.6')
TMP_text.configure(anchor='w', font='{clean} 20 {}', height='1', text='97.6')
TMP_text.configure(textvariable=TMP, width='4')
TMP_text.place(anchor='nw', relx='0.18', rely='0.08', x='0', y='0')
BPM_text = tk.Label(frame1)
BPM_text.configure(background='#505351', font='{clean} 14 {}', foreground='#ffffff', text='Blood Pressure')
BPM_text.place(anchor='nw', rely='0.4', x='0', y='0')
Systolic_text = tk.Label(frame1)
Systolic_text.configure(background='#505351', compound='top', font='{clean} 12 {}', foreground='#ffffff')
Systolic_text.configure(text='Systolic')
Systolic_text.place(anchor='nw', relx='0.0', rely='0.5', x='0', y='0')
Diastolic_text = tk.Label(frame1)
Diastolic_text.configure(background='#505351', font='{clean} 12 {}', foreground='#ffffff', text='Diastolic')
Diastolic_text.place(anchor='nw', rely='0.65', x='0', y='0')
Systolic = tk.Label(frame1)
Systolic_val = tk.IntVar(value=120)
Systolic.configure(font='{clean} 20 {}', text='120', textvariable=Systolic_val)
Systolic.place(anchor='nw', relx='0.2', rely='0.48', x='0', y='0')
Diastolic = tk.Label(frame1)
Diastolic_val = tk.StringVar(value='100')
Diastolic.configure(font='{clean} 20 {}', text='100', textvariable=Diastolic_val)
Diastolic.place(anchor='nw', relx='.2', rely='0.64', x='0', y='0')
BPM_start = tk.Button(frame1)
BPM_go = tk.StringVar(value='Start')
BPM_start.configure(height='1', text='Start', textvariable=BPM_go, width='3')
BPM_start.place(anchor='nw', relx='0.0', rely='0.76', x='0', y='0')
# BPM_start.configure(command=BPM_go_func)
BPM_stop = tk.Button(frame1)
BPM_st = tk.StringVar(value='Stop')
BPM_stop.configure(font='TkMenuFont', height='1', text='Stop', textvariable=BPM_st)
BPM_stop.configure(width='3')
BPM_stop.place(anchor='nw', relx='0.15', rely='0.76', x='0', y='0')
# BPM_stop.configure(command=BPM_st_func)
ECG_text = tk.Label(frame1)
ECG_text.configure(background='#505351', font='{clean} 14 {}', foreground='#ffffff', text='ECG')
ECG_text.place(anchor='nw', relx='0.4', x='0', y='0')
HR_text = tk.Label(frame1)
HR_text.configure(background='#505351', cursor='arrow', font='{clean} 12 {}', foreground='#ffffff')
HR_text.configure(takefocus=False, text='Heart rate (BPM):')
HR_text.place(anchor='nw', relx='0.4', rely='.1', x='0', y='0')
HR_value = tk.Label(frame1)
HR_val = tk.StringVar(value='103')
HR_value.configure(anchor='e', font='{clean} 20 {}', text='103', textvariable=HR_val)
HR_value.place(anchor='nw', relx='0.8', rely='0.07', x='0', y='0')
ECG_go = tk.Button(frame1)
ECG_go.configure(text='Start')
ECG_go.place(anchor='nw', relx='0.4', rely='0.57', x='0', y='0')
# ECG_go.configure(command=ECG_go_func)
ECG_st = tk.Button(frame1)
ECG_st.configure(text='Stop')
ECG_st.place(anchor='nw', relx='0.65', rely='.57', x='0', y='0')
# ECG_st.configure(command=ECG_st_func)
Export_data = tk.Button(frame1)
Export_data.configure(text='Export Data')
Export_data.place(anchor='nw', relx='0.35', rely='0.85', x='0', y='0')
# Export_data.configure(command=data_exp)
Dev_stat = tk.Label(frame1)
Dev_stat.configure(background='#505351', font='{clean} 14 {}', foreground='#ffffff', text='Device Status:')
Dev_stat.place(anchor='nw', relx='0.35', rely='.7', x='0', y='0')
Status = tk.Label(frame1)
stat = tk.StringVar(value='Good')
Status.configure(font='{clean} 36 {}', text='Good', textvariable=stat)
Status.place(anchor='nw', relx='0.7', rely='.7', x='0', y='0')
canvas1 = tk.Canvas(frame1)
canvas1.configure(relief='raised')
canvas1.place(anchor='nw', height='100', relx='0.4', rely='0.2', width='220', x='0', y='0')
frame1.configure(background='#505351', height='300', width='400')
frame1.grid(column='0', row='0')

# Main widget
mainwindow = frame1

if __name__ == '__main__':
    # #serial setup
    # ser = serial.Serial("COM8", 9600, timeout=1)
    # ser.flush()
    #gui setup
    root.mainloop

# while True:
#     ser_text = str(ser.readline().decode('utf-8').rstrip)
#     if ser_text.startswith('TMP = ') == True:
#         TMP_decode(ser_text)
#     elif ser_text.startswith('BPM = ') == True:
#         BPM_decode(ser_text)
#     elif ser_text.startswith('ECG = ') == True:
#         ECG_decode(ser_text)

# def TMP_func(str):
#     TMP_in = int(str.strip('TMP = '))
#     print(TMP_in)


# while True:
#     IDK = input('tmp value')
#     print(IDK)
#     TMP = IDK

    # if ser.in_waiting > 0:
    #     line = str(ser.readline().decode('utf-8').rstrip())
    #     if ECG in line == True:
    #         ECG(line)
    #         return
    #     if BPM in line == True:
    #         BPM(line)
    #         return
    #     if TMP in line == True:
    #         TMP(line)
    #         return

# xvals = np.arange(1,100,1)
# yvals = []
# plt.cla()

# plt.plot(xvals, yvals, label='ECG_data')

#ani= FuncAnimation(plt.gcg(), animate, interval=1000)


#plt.tight._layput() ##being used
# plt.show()
