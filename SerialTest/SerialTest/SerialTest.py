import serial
print ("hello")
ser = serial.Serial("COM3",9600)

while True:
    content = ser.read()
    print (content)
    print ("\n")
    
