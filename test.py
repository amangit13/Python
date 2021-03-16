class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("bob")
print(dog.name)
hex = bytearray([0xEF]*10)
print (hex)
file = open("rom.bin", "wb")
file.write(hex)
file.close()

file = open("rom.bin", "rb")
content = file.read()
file.close()

print (content)
