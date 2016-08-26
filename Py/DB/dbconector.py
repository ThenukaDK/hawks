import MySQLdb
import os

def searchFiles():
    nameArray = []
    for filename in os.listdir("."):
        if filename.endswith("jpg"):
            nameArray.append(filename)

    
db = MySQLdb.connect(host="127.0.0.1",
                     user="root",         
                     passwd="root",  
                     db="drones")        

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

'''
# Use all the SQL you like
cur.execute("SELECT * FROM image_map")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0] +" |"+ row[1] +" |"+ row[2] +" |"+ row[3] +" |"+ row[4]
'''



db.close()
