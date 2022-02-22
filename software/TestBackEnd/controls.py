import time;
import RPi.GPIO as GPIO


class Controls:
 DriverX = 0
 DriverY = 0
 DriverZ = 0
 DriverOmega = 0
 def __init__(self):
  GPIO.setwarnings(False) 
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
 makeStepPin = None
 rotationPin = None
 resetComPin = None

 def __init__(self,MakeStepPin, RotationPin, ResetComPin):
    global resetComPin, makeStepPin, rotationPin
    GPIO.setwarnings(False) 
    print("Initializaiton driver")
    makeStepPin = MakeStepPin
    rotationPin = RotationPin
    resetComPin = ResetComPin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(makeStepPin, GPIO.OUT)
    GPIO.setup(rotationPin, GPIO.OUT)
    GPIO.setup(resetComPin, GPIO.IN)
    
 def MakeStep(self, Steps, Rotation):
  tempStepMem = Steps
  print(resetComPin)
  print(makeStepPin)
  while(tempStepMem > 0):
   if(GPIO.input(resetComPin) == 0):
    if(Rotation == 1):
     GPIO.output(rotationPin, GPIO.HIGH)
    else:
     GPIO.output(rotationPin, GPIO.LOW)
    GPIO.output(makeStepPin, GPIO.HIGH)
    time.sleep(0.010)
    GPIO.output(makeStepPin, GPIO.LOW)
    tempStepMem-=1
    print('step')
   time.sleep(0.010)
  return

 def end(self):
  print('end')
  GPIO.cleanup()

d = Driver(35,36,1);
d.MakeStep(3,0)
d.end();
    
