
import time;
import RPi.GPIO as GPIO



class Controls:
 Drivers = []
 DriverX = 0
 DriverY = 0
 DriverZ = 0
 DriverE = 0
 def __init__(self):
  global DriverX, DriverY, DriverZ,DriverE, Drivers
  GPIO.setwarnings(False) 
  print("Controls init-ed")

  #init-ing drivers
  DriverX = Driver(0,0,0)
  DriverY = Driver(0,0,0)
  DriverZ = Driver(0,0,0)
  DriverE = Driver(0,0,0)
  
  #adding drivers to be configured easilie
  Drivers.append(DriverX)
  Drivers.append(DriverY)
  Drivers.append(DriverZ)
  Drivers.append(DriverE)

 def SetupDriver(self, index, pinStep, pinRot, pinCom):
   global Drivers
   if(index.isdigit()):
     Drivers[inDriver] = Driver(pinStep, pinRot, pinCom)
   else:
     print("Error - The driver setup value needs to be number SetupDriver()")
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
  if(Steps <= 0):
    return 1
  
  tempStepMem = Steps

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
    time.sleep(0.010)
  return 0

 def Clear(self):
  print('Cleaning GPIO')
  GPIO.cleanup()