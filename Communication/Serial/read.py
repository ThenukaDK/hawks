import serial
import time
import base64

PORT = 'COM32' # The port my Arduino is on

print("start reading data on port",PORT)

ser = serial.Serial(PORT , 9600)


tempPath = "./temp/"
outPath = "./out/"

while True:

    
    if ser.inWaiting():
        st=ser.readline()
        print(st)

        fo = open(tempPath+"split8.txt", "ab")
        fo.write(st)
        fo.close()

        pp=st
        pp=pp.decode("utf-8") 

        #if the star detected it will end 
        if(pp.find("*")!=-1):
            print("exiting")
            break

ser.close()



#combind parts
with open(tempPath+"split8.txt") as f:
    content = f.readlines()
k=""
for i in content:
	# print(i[2:-3])
	k=k+i[2:-3]


k=k[2:-4]
k=k.replace('\\n', '')
k=k.replace('*', '')
k=k[:-1]
print(k)


# # Open a file
fo = open(tempPath+"t2.txt", "w")
fo.write(k);
fo.close()


image = open(tempPath+'t2.txt', 'rb')
image_read = image.read()
image.close()
print(image_read)


#add padding correction

def decode_base64(data):

    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)


image_result = open(outPath+'1.jpg', 'wb') # create a writable image and write the decoding result
image_result.write(decode_base64(image_read ))

image_result.close()
