import server
import threading
import time

def start():
 server.StartServer()
 return

def controlled():
 print("Done! - Controlls started")
 while(True):
     time.sleep(1)
     try:
      CheckGCode(server.queue.pop(0))
     except:
      pass
 return 
def split(word):
    return [char for char in word]
     
def CheckGCode(gCode):
 Splitted = gCode.split()
 if (split(Splitted[0])[0] == "G"):
  print("Command - G")   

  gcommandNum = ""
  for y in split(split(Splitted[0])):
    if y.isdigit():
                gcommandNum += str(y)
  print("Number - " + gcommandNum)    
  if(gcommandNum == "1" or gcommandNum == "0" ):
      for x in Splitted:
        axis = split(x)[0]
        movementMore = ""
        for y in split(x):
            if y.isdigit():
                movementMore += str(y)
        if(axis == "X"):
            print(f"Printing X - {movementMore}")
        elif(axis == "Y"):
            print(f"Printing Y - {movementMore}")
        elif(axis == "Z"):
            print(f"Printing Z - {movementMore}")
        elif(axis == "E"):
            print(f"Printing E - {movementMore}")
 else: return 1
 return 0


if(__name__ == '__main__'):
 print("Starting threads")
 x = threading.Thread(target=start, daemon=True)
 y = threading.Thread(target=controlled , daemon=True)

 print("Server thread Starting")
 x.start()
 time.sleep(.1)
 print("Controll thread Starting")
 y.start()
 while(True):
     time.sleep(1)
 print("Program exited")