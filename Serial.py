import serial
import time

print ("hello")

ports = ['com3', 'com4', 'com5']

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
    if (content[0] == 32):
        i+=1
    else:
        if i>4:
            i=0
            print ("")

        print (hex(content[0]), end='')
        print (" ",end="")

  
