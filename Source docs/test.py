import serial
import serial.tools.list_ports

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
]
port = str(arduino_ports[0])
ser = serial.Serial(port=port, baudrate=9600)
print(port)

stack = [b'0 0 0 0\r\n']
# ^this is just a random value to compare against init
while True:
    ser_bytes = ser.readline()
    stack.append(ser_bytes)
    print(ser_bytes, stack)
    if ser_bytes != stack[0]:
        print("true")
        stack.pop(0)
    else:
        stack.pop(0)