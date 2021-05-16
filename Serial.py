import serial
import time

print ("hello")

LINE_FEED = 10

TEXT=1
NUM=0
format = TEXT

ports = ['com3', 'com4', 'com5', 'com6', 'com7']

while 1:
    for port in ports:
        print ("opening serial " + port)
        try:
            ser = serial.Serial(port,9600)
            break
        except Exception as e:
            print ("error opening " + str(e))
        time.sleep(.2)
    break

print("success")
i=0

while True:
    content = ser.read()

    if format == TEXT:
        if content[0] == LINE_FEED:
            print ("")
        else:
            print (chr(content[0]), end="")
    else:
        print (hex(content[0]), end='')
        print (" ",end="")

        i+=1
        if i>10:
            i=0
            print ("")
 
  
