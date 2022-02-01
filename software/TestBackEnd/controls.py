#GPIO import
import time;

class Controls:
 def __init__(self):
     print("Controls init-ed")


 def makeSteps(self, axis, steps, rotation):
  while(steps > 0):
   if axis=="x":
    print("driver1")
    print(rotation)
    #driver;
   elif axis=="y":
    print("driver2")
    print(rotation)
    #driver2
   elif axis=="z":
    print("driver3")
    print(rotation)
    #driver3 
   steps-=1
