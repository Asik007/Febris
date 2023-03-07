import csv
import time
from time import strftime, localtime
import serial.tools.list_ports

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
]
port = str(arduino_ports[0])
ser = serial.Serial(port=port, baudrate=9600)

name_raw = time.strftime("%d %b %Y", localtime())+"RAW.csv"
print("pog")
while True:
    data_time = []
    data_serial = []
    data_one = []
    data_two = []
    data_three = []
    data_four = []
    for i in range(10):
        ser_bytes = ser.readline()
        if len(ser_bytes) > 8:
            decoded_bytes = str(ser_bytes.decode("utf-8").strip())
            # print(data_time,data_serial)
            data_time.append(strftime("%X", localtime()))
            data_serial.append(decoded_bytes)
            data = decoded_bytes.split(" ", 4)
            # print(data[0])
            data_one.append(data[0])
            data_two.append(data[1])
            data_three.append(data[2])
            data_four.append(data[3])
            print(data)
    with open(name_raw, "a", newline='') as f:
        writer = csv.writer(f, delimiter=",")
        row = zip(data_time, data_serial, data_one, data_two, data_three, data_four)
        writer.writerows(row)
        print(list(zip(data_time, data_serial, data_one, data_two, data_three, data_four)))