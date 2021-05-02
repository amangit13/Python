import serial
import time

print ("hello")
ser = serial.Serial("COM4",9600)
i=0
while True:
    content = ser.read()
    if (content[0] == 32):
        print ("\t", end='')
        i+=1
    else:
        if i>3:
            i=0
            print ("")
        print (hex(content[0]), end='')
        print (" ",end="")

        input()
