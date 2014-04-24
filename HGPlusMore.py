# Author Pei-Chen Tsai aka Hammer
#email : please use gitHub issue system
import sys
import os
from subprocess import Popen
from subprocess import PIPE

global COI #user of changeset(commit)
#|changeset|user|
COI = []
global COI_REV, COI_USR
#clean user list no duplicate!
COI_REV, COI_USR = range(2)
USRARY = []

#[]== algorithm could be better
def isUserInsideUSRARY(name):
   for usr in USRARY :
      if name == usr :
         return True
   return False

def prepareCleanUsrAry():
   for entry in COI:
     name = entry[COI_USR]
     if isUserInsideUSRARY(name) == False :
        USRARY.append(name)
   print "%d users found" %(len(USRARY))

def parsePIPE():
   UOI = []
   state = 0
   for line in sys.stdin:
      line = line.replace(" ","")
      #print line
      lineAry = line.split(":")      
      #print lineAry[0]
      if lineAry[0] == 'changeset' :
         UOI = []
         UOI.append(lineAry[1])
      if lineAry[0] == 'user' :
         UOI.append(lineAry[1])
         COI.append(UOI)

   print '%d commit found' %(len(COI))
   #print COI

def main():
   #print "hg log | python HGPlus.py <DB>" 
   #print "ctrl+d if you don't pipe in any thing"
   #verify()
   #print "===== OUTPUT START ====="
   parsePIPE() #output total commits, also.
   prepareCleanUsrAry() #output total users, also.

if __name__ == "__main__":
   main()
