
#Network Libraries - Back End
from flask import Flask, request, jsonify;
from flask_cors import CORS;
from flask import jsonify, request



#Custom Libraries
#from controls import Controls

#Important Libraries
from io import BytesIO
import threading
import time;
import sys;
import os
import array

queue = []
data = ""
queue.append(data)
#Instalization with CORS for security stuff. Packages won't be accepted otherwise
app = Flask(__name__)
CORS(app)


#Controller = Controls()

#Inforamtion
workingStatus = False
workingPercentage = 0


@app.route('/uploadOneGCode', methods=['POST'])
def upload_one_g_code():
    d = {}
    print()
   # r = (request.data.gcodes)
    try:
        gcode = request.get_json()['gcodes']
        
        queue.append(gcode)
        d['status'] = 1

    except Exception as e:
        print(f"Couldn't upload file {e}")
        d['status'] = 0

    return jsonify(d)


@app.route('/upload_file', methods=['POST'])
def upload_file():
    d = {}
    try:
        file = request.files['file_from_react']
        filename = file.filename
        print(f"Uploading file {filename}")
        file_bytes = file.read()
        array = str(file_bytes,'UTF-8').splitlines()
        f = open(f"./gCodes/{filename}", "w")
        for ar in array:
            f.write(ar + "\n")
        f.close()
        d['status'] = 1

    except Exception as e:
        print(f"Couldn't upload file {e}")
        d['status'] = 0

    return jsonify(d)

@app.route('/getgcode', methods=['Get'])
def getgCode():
    d = {}
    try:
        FilesToReturn = []
        files = os.listdir('./gCodes')
        for f in files:
            FilesToReturn.append(f)
        d['status'] = 1
        d['files'] = FilesToReturn
    except Exception as e:
        print(f"Couldn't upload file {e}")
        d['status'] = 0

    return jsonify(d)


@app.route('/openFile', methods=['Post'])
def openGCode():
    d = {}
    try:
        index = request.get_json()['fileIndex']
        foundIndex =0
        files = os.listdir('./gCodes')
        for f in files:
            if(index == foundIndex):
                print(f)
                break
            foundIndex +=1

        d['status'] = 1
    except Exception as e:
        print(f"Couldn't upload file {e}")
        d['status'] = 0

    return jsonify(d)


@app.route('/')
def hello():
    response = jsonify(
      Working=False,
      WorkingPercentage=25
    )
   # response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/moveAxis', methods=['POST'])
def moveAxis():
 data = request.json
 
 # sends to the (controls.py) library which axis to controll
 #Controller.makeSteps(data["axis"],data["steps"],data["rotation"])
 
 response = jsonify(status=0)
 response.headers.add('Access-Control-Allow-Origin', '*')
 return response



def StartServer():
 print("Done! - Starting Server")
 app.run(host="127.0.0.1",debug=False)
 #app.run()
 
