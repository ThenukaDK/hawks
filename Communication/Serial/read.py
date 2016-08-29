import serial
import time
import base64

PORT = 'COM20' # The port my Arduino is on, on my WinXP box.

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

        if(pp.find("*")!=-1):
            print("exiting")
            break

ser.close()




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

# print("type is ",type(k))

# # Open a file
fo = open(tempPath+"t2.txt", "w")
fo.write(k);

# Close opend file
fo.close()


image = open(tempPath+'t2.txt', 'rb')
image_read = image.read()
image.close()
print(image_read)

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)

# image_64_decode = base64.decodestring(image_read)
image_result = open(outPath+'1.jpg', 'wb') # create a writable image and write the decoding result
image_result.write(decode_base64(image_read ))

image_result.close()
