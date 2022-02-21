import time;
import RPi.GPIO


class Controls:
  DriverX = 0
  DriverY = 0
  DriverZ = 0
  DriverOmega = 0
 def __init__(self):
  print("Controls init-ed")
  DriverX = Driver(0,0,0)
  DriverY = Driver(0,0,0)
  DriverZ = Driver(0,0,0)
  DriverOmega = Driver(0,0,0)

 def makeSteps(self, axis, steps, rotation):  
  if axis=="x":
    DriverX.MakeStep(steps,rotation)


  elif axis=="y":
    DriverY.MakeStep(steps,rotation)


  elif axis=="z":
    DriverZ.MakeStep(steps,rotation)
 return



class Driver:
 makeStepPin = 0
 rotationPin = 0
 resetComPin = 0

 def __init__(self,MakeStepPin, RotationPin, ResetComPin):
    print("Initializaiton driver")
    makeStePin = MakeStepPin
    rotationPin = RotationPin
    resetComPin = ResetComPin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(makeStePin, GPIO.OUT)
    GPIO.setup(rotationPin, GPIO.OUT)
    GPIO.setup(resetComPin, GPIO.IN)
 
 def MakeStep(self, Steps, Rotation):
    tempStepMem = Steps
    while(tempStepMem > 0):
       if(GPIO.input(resetComPin) = 0):
         if(Rotation == 1):
           GPIO.output(rotationPin, GPIO.HIGH)
         else:
           GPIO.output(rotationPin, GPIO.LOW)
        GPIO.output(makeStePin, GPIO.HIGH)
        time.sleep(0.010)
        GPIO.output(makeStePin, GPIO.LOW)
        tempStepMem-=1
      time.sleep(0.010)
    return

 def end(self):
   GPIO.cleanup()

    
