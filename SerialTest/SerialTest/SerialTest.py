import serial
print ("hello")
ser = serial.Serial("COM5",9600)

while True:
    content = ser.read()
    print (chr(content[0]), end='')
