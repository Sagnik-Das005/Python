import os
import time
D={(0,0):"   ",(0,1):"   ",(0,2):"   ",\
   (1,0):"   ",(1,1):"   ",(1,2):"   ",\
   (2,0):"   ",(2,1):"   ",(2,2):"   "}
RD=dict(D)
f=1
turns=0
n=1
print(D[(0,0)],"|",D[(0,1)],"|",D[(0,2)])
print("----------------") 
print(D[(1,0)],"|",D[(1,1)],"|",D[(1,2)])
print("----------------")
print(D[(2,0)],"|",D[(2,1)],"|",D[(2,2)])
while n!=0:
    pos=eval(input("Enter"))
    if not(0<=pos[0]<=2) or  not(0<=pos[1]<=2) and len(pos)==2 and type(pos)==type(()):
        print("Invalid Input Try Again")
        continue
    if f==0:
        f=1
        plc=" X "
        r=0
    else:
        f=0
        plc=" O "
        r=1
    
    if D[pos]=="   ":
        D[pos]=plc
        turns+=1
    else:
        print("WRONG MOVE START AGAIN")
        D=dict(RD)
        turns=0
        time.sleep(2)
        os.system("cls")
        
    os.system('cls')
  
    print(D[(0,0)],"|",D[(0,1)],"|",D[(0,2)])
    print("----------------") 
    print(D[(1,0)],"|",D[(1,1)],"|",D[(1,2)])
    print("----------------")
    print(D[(2,0)],"|",D[(2,1)],"|",D[(2,2)])

    if(D[(0,0)]==D[(0,1)]==D[(0,2)] and D[(0,0)]!="   "):
        print(D[(0,0)],"WINS")
        break
    
    elif(D[(1,0)]==D[(1,1)]==D[(1,2)] and D[(1,0)]!="   "):
        print(D[(1,0)],"WINS")
        break
        
    elif(D[(2,0)]==D[(2,1)]==D[(2,2)] and D[(2,0)]!="   "):
        print(D[(2,0)],"WINS")
        break
    elif(D[(0,0)]==D[(1,0)]==D[(2,0)] and D[(0,0)]!="   "):
        print(D[(0,0)],"WINS")
        break
    
    elif(D[(0,1)]==D[(1,1)]==D[(2,1)] and D[(0,1)]!="   "):
        print(D[(0,1)],"WINS")
        break
   
    elif(D[(0,2)]==D[(1,2)]==D[(2,2)] and D[(0,2)]!="   "):
        print(D[(0,2)],"WINS")
        break

    elif(D[(0,0)]==D[(1,1)]==D[(2,2)] and D[(0,0)]!="   "):
        print(D[(0,0)],"WINS")
        break

    elif(D[(0,2)]==D[(1,1)]==D[(2,0)] and D[(0,2)]!="   "):
        print(D[(0,2)],"WINS")
        break
    if turns==9:
        print("DRAW")
        break
time.sleep(3)
