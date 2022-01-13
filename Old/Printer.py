# imports Libraries
print("importing Libraries")
from enum import Enum
import serial
import threading
import queue
# State

Port = "COM3"
Speed = 115200
TimeOut = 0


print("Setting Variables")
class State(Enum):
    Waitting = 0
    Printing = 1
state = State.Waitting
lastState = queue.Queue()
openPort = False
#Setup overall
print("Setting Up Loggic");
# Main Thread
def ThreadLogger(state,out_queue):
    while True:
        output = ChecksState(state)
        out_queue.put(output)
        #ask for state
        
# Inside Main Thread Checks for changes
def ChecksState(StateIs):
        #check state
    if StateIs == State.Waitting:
        StateIs = State.Printing
    return StateIs

def OpenSerial():
    try:
        ser = serial.Serial(Port, Speed, timeout=TimeOut)
        openPort = True
    except serial.SerialTimeoutException:
        print("[INFO] Serial timeout")
        openPort = False
    except serial.SerialException:
        print("[ERROR] Problem while trying to open " + str(Port) + ". Is the device pluged in?")
        openPort = False
    if openPort == True:
        print("Port " + str(Port) + " is open")
    elif openPort == False:
        print("Port " + str(Port) + " is closed")
    return openPort, ser

# MainLogic
if __name__ == "__main__":


    openPort, ser = OpenSerial()
    print("Creating Thread")
    MainThread = threading.Thread(target=ThreadLogger, args=(state,lastState,))
    MainThread.setName("Main Thread")
    print("Starting Thread")
    if openPort == True:
        MainThread.start()
        print(str(MainThread.getName()) + " is alive :: " + str(MainThread.is_alive()))
        #get data from threat
        print("Getting state")
        if lastState.empty():
            print("[ERROR] the reterned queue (value) from the Thread is empty")
        else:
            state = lastState.get()
            print("State fround :: " + str(state))
        print("End of Main Logic")
    elif openPort == False:
        print("[INFO] Port " + str(Port) + " wasn't open and the Thread wasn't started")
    doge = ""
    while True:
        print(MainThread.is_alive())
        console = input()
        if console == "thread on":
            MainThread.start()
        elif console == "reset":
            MainThread.join()

#wait
input("Program Ended")
