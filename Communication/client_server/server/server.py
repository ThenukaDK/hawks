import socket
import sys
import os
import zipfile
from Crypto import Random
from Crypto.Cipher import AES


#------------ encryption function start ---------------------------

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)

#------------ encryption function end ---------------------------









print("\n################## Starting Server file #################\n")


#key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'          #key for encrypting and decrypting
key='aaaabbbbccccdddd'


host = socket.gethostname() # Get local machine name
#host="192.168.137.1"
port = 12345 # Reserve a port for your service.

print("server host name ",host," port is ",port)
print("starting server.....")


s = socket.socket() #create a socket
s.bind((host,port)) #bond the host and port

print("server started, waiting for client\n")
s.listen(10) # waiting to accept 10 connection


i=1 #file counting variable

path="./rec/"

while True:
    sc, address = s.accept()                #accept client connection
    print ("\ndata receving from ",address)

    naming="pic_c1"+str(i)+".jpg.enc"       #rename files

    completePath=path+naming                #get the file path and file name

    f = open(completePath,'wb')             #open in binary
    print("%d. %s recieved"%(i,naming))

    i=i+1
    l = 1
    while(l):                               #We receive and write to the file
        l = sc.recv(1024)
        while (l):
            f.write(l)
            l = sc.recv(1024)
        f.close()






#-----------------------decrypting start ---------------------------
    print('decrypting ',naming)             
    decrypt_file(completePath, key)         #decrypting file
    print("Deleting: ",naming)
    os.remove(completePath)             #delete orginal file
#-----------------------decrypting end ---------------------------



    sc.close()
s.close()


print("\n################## Ending Server file #################\n")