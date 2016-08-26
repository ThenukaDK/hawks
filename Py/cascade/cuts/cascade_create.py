import urllib2
import urllib
import cv2
import numpy as np
import os


def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n13108545'
    neg_image_urls = urllib2.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')


    pic_num = 882

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i, "neg/"+str(pic_num)+'.jpg')
            img = cv2.imread("neg/"+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)
            pic_num +=1

        except Exception as e:
            print(str(e))
    



def find_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)

                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('ugly removed')
                        print(current_image_path)
                        os.remove(current_image_path)


                except Exception as e:
                    print(str(e))

def create_pos_n_neg():
    for file_type in ['pos']:
        for img in os.listdir(file_type):
            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('cuts.info','a') as f:
                    f.write(line)


def open_n_graysacale():
   for i in range(1,131):
       image = cv2.imread('negatives/'+str(i)+'.jpg',cv2.IMREAD_GRAYSCALE)
       resized_image = cv2.resize(image, (100,100))
       cv2.imwrite("neg/"+str(i)+'.jpg', resized_image)



#open_n_graysacale()
         
create_pos_n_neg()
#find_uglies()                    
#store_raw_images()
