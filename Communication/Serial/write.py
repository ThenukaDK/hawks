#!/usr/bin/python
import serial
#import syslog
import time
import base64




import os, sys

path = "./in/"
dirs = os.listdir( path )
print(dirs)


print()
print()

for pic in dirs:

	fullPath=path+pic
	print("\nsending file ",fullPath,"\n")
	image = open(fullPath, 'rb')
	image_read = image.read()
	image_64_encode = base64.encodestring(image_read)

	#print(image_64_encode)

	print()
	print()

	x=image_64_encode
	#x=x.replace(" ", "")
	x=str(x)
	x=x+"*"
	print(x)

	#The following line is for serial over GPIO
	port = 'COM11' # note I'm using Mac OS-X


	y=[]
	z=[]
	a=0
	b=2
	k=0

	jump=8

	while k<len(x):

		a=k
		b=a+jump
		#print("a %d b %d"%(a,b))
		y.append([''.join(x[a:b])])
		k=k+jump
		

	p=0

	print("No of characters to send : %d"%len(x))
	print("No of parts to send : %d"%len(y))
	print("Sending size : %d"%jump)
	print("estimate time %d seconds (%f minutes) "%(3*len(y),3*len(y)/60))
	print()

	for i in y:
		#print(i)

		p=p+1
		ard = serial.Serial(port,9600,timeout=5)
		time.sleep(2) # wait for Arduino

		sending=str(i)
		sending=sending+sending[-1:]
		sending=bytes(sending, encoding="ascii")

		print("Python value sent: ",sending)
		print("-------------------------------------------- %d %%"%(p/len(y)*100))

		ard.write(sending)
		time.sleep(1) # I shortened this to match the new value in your Arduino code
		ard.close()


