import serial
import time

print ("hello")
ser = serial.Serial("COM4",9600)

while True:
    content = ser.read()
    print (chr(content[0]), end='')
