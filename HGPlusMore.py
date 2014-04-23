# Author Pei-Chen Tsai aka Hammer
#email : please use gitHub issue system
import sys
import os
from subprocess import Popen
from subprocess import PIPE

global COI #user of changeset(commit)
#|changeset|user|
COI = []

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
         UOI.append(lineAry[2])
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
   parsePIPE()

if __name__ == "__main__":
   main()
