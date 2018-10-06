
#############################################
#                 Bragi                     #
#   Main file for backend project           #
#   Check /docs/documentation.md for info   #
#   contact:jaimegbonorino@gmail.com        #
#############################################

import utils, config
from flask import Flask, json, jsonify, request #FlaskAPI for backend
from flask_cors import CORS, cross_origin

#Todos los mocks aca
networksMock = {  
        "network":[  
                "Facebook",
                "Twitter",
                "Discord",
                "Telegram",
                "Slack"
        ]
}

#Iniciamos la aplicacion flask
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#Listado de endpoints

#Endpoint saludo
@app.route('/')
def helloWorld():
    hello = """Hail, Æsir!
                Hail, Asyniur!
                And ye, all-holy gods!
                all, save that one man,
                who sits within there,
                Bragi, on yonder bench."""
    return jsonify(hello) #El fetchApi de react se pone quisquilloso si no mandas json

#Get all social networks
@app.route('/networks')
def getNetworks():
    return networksMock