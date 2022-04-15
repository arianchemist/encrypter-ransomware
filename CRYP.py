# crypter {< dangerous >}
#import hashlib

from cryptography.fernet import Fernet
import os
import time

NDC = open("passwords.txt" , "r")
V = NDC.read()
key = Fernet.generate_key()
fernet = Fernet(key)
B = fernet.encrypt(V.encode())
NDC.close()

os.remove("passwords.txt")

NEWF = open("ENC.ENC" , "w")
NEWF.write(B.decode())
NEWF.close()

time.sleep(10)

U = input("wanna see your password ? type y < ")

if U == "y":
    print("wait")
    time.sleep(2)
    for g in range(10):
        print(str(g) + "0")
        time.sleep(1)
    print("your password is : " + V)
else:
    print("error")