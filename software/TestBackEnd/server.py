
#Network Libraries - Back End
from flask import Flask, request, jsonify;
from flask_cors import CORS;


#Custom Libraries
from controls import Controls
from moduleControl import ModuleControls

#Important Libraries
import threading
import time;
import sys;


#instalization
app = Flask(__name__)
CORS(app)
cont = Controls()
module = ModuleControls()

#Inforamtion
printingStatus = False


@app.route('/')
def hello():
    response = jsonify(
      printing=printingStatus,
      printingState=0
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/moveAxis', methods=['POST'])
def moveAxis():
 data = request.json
 cont.makeSteps(data["axis"],data["steps"],data["rotation"])
 response = jsonify(status=0)
 response.headers.add('Access-Control-Allow-Origin', '*')
 return response



if(__name__ == '__main__'):
 print("Starting Server")
 #app.run(host="192.168.0.105",debug=True)
 app.run()
 
