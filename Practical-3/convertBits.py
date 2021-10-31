# 2. Write a program to convert bits to Megabytes, Gigabytes and Terabytes
bits = int(input("Enter Bites :"))
byte = bits / 8
kb = byte / 1024
mb = kb / 1024
gb = mb / 1024
tb = gb / 1024
print("Megabytes =", mb, "\n Gigabytes =", gb, "\n Terabytes =", tb)
