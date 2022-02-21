#GPIO import
import time;

class Controls:
 def __init__(self):
     print("Controls init-ed")


 def makeSteps(self, axis, steps, rotation):
  DriverX = Driver(0,0,0)
  
  if axis=="x":
    print("driver1")
    print(rotation)
    DriverX.MakeStep(15,1)
    #driver;
  elif axis=="y":
    print("driver2")
    print(rotation)
    #driver2
  elif axis=="z":
    print("driver3")
    print(rotation)
    #driver3 


class Driver:
 makeStepPin = 0
 rotationPin = 0
 resetComPin = 0

 def __init__(self,MakeStepPin, RotationPin, ResetComPin):
    print("Initializaiton driver")
    makeStePin = MakeStepPin
    rotationPin = RotationPin
    resetComPin = ResetComPin
 
 def MakeStep(self, Steps, Rotation):
    tempStepMem = Steps
    while(tempStepMem > 0):
        #if(resetComPin = 0):
        # step
        print("making Step: " + str(tempStepMem))
        tempStepMem-=1
    return
    
