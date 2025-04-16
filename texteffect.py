import random
import time
import os
from colorama import init

init()
txt=input("Enter a text \n")
t=""
os.system("cls")

for i in txt:
    c=""
    print(t,end="")

    while c!=i:
        print("\r",end="")
        print(len(t)*"\033[C",end='')
        c=chr(random.randint(32,127))
        print(c,end="")
        time.sleep(0.025)

    if(c==i):
        print("\r",end="")
        t=t+c
   
    time.sleep(0.025)

print(t)
time.sleep(2)
exit=input("Press enter to exit")
