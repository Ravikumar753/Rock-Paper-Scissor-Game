import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSOR=3

#Nama input kudukuratuku 

print(" ")
playerchoice=input("Enter....\n\n 1 for Rock \n 2 for Paper \n 3 for Scissor \n \n ")

# print(playerchoice)
# print(type(playerchoice))

player=int(playerchoice) 

if player<1 or player>3:
    sys.exit("MENTAL PUNDA  \n ONLY ENTER 1 ,2 or 3")
    
#Computer input kudukuratuku

computerchoice=random.choice("123")
computer=int(computerchoice)

#Output Screen ahkuratuku

print(" ")
print("You Choose" +" "+str (RPS(player)).replace('RPS.','') + ".")
print("Python Choose" +" "+ str (RPS(computer)).replace('RPS.','') + ".")
print(" ") 

#if and else format for output printing

if player==1 and computer==3:
    print("😎 YOU WIN !")
elif player==2 and computer==1:
    print("😎 YOU WIN !")
elif player==3 and computer==2:    
    print("😎 YOU WIN !")
elif player==computer:
    print("😯 GAME DIE !")
else:
    print("🐍 PYTHON WIN !")        
    
print(" ")
print(" ")
