
#Network Libraries - Back End
from flask import Flask, request, jsonify;
from flask_cors import CORS;


#Custom Libraries
from controls import Controls


#Important Libraries
import threading
import time;
import sys;


#instalization
app = Flask(__name__)
CORS(app)
cont = Controls()


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


@app.route('/post_test', methods=['GET','POST'])
def post_test():
 data = request.json
 cont.makeSteps(data["axis"],data["steps"],data["rotation"])
 response = jsonify(status=0)
 response.headers.add('Access-Control-Allow-Origin', '*')
 return response



if(__name__ == '__main__'):
 app.run(host="192.168.0.106",debug=True)

 
