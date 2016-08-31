import time
import numpy as np
import os



def job():
   with open("../spliting/vedioCap.py") as f:
      code = compile(f.read(), "vedioCap.py", 'exec')
      exec(code)

   with open("../spliting/removeFiles.py") as f2:
      code = compile(f2.read(), "removeFiles.py", 'exec')
      exec(code)
   

if __name__ == '__main__':
    while True:
        job()
        time.sleep(5)
