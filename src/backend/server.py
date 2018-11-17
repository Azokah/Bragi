from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS, cross_origin
import json, client

# from client import send_msg

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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

@app.route('/slack/', methods=['GET'])
def index():
    data = {}
    data['getUsers'] = '[{"msg":"GET, devuelve los usuarios"}]'
    data['getChannels'] = '[{"msg":"GET, devuelve los channels"}]'
    data['sendMsg'] = '[{"msg":"POST, envia mensaje", "param-1": "mensaje", "param-2": "channel"}]'
    return json.dumps(data)

@app.route('/slack/getUsers', methods=['GET'])
def slackGetUsers():
    return jsonify(client.user_list())

@app.route('/slack/getChannels', methods=['GET'])
def slackGetChannels():
    return jsonify(client.list_channel())

@app.route('/slack/sendMsg', methods=['POST','GET'])
def slackPostMessage():
    if request.method == 'POST':
        data = request.get_json(force=True)
        if (client.send_msg(data["mensaje"], data["channel"])):
            return jsonify(returnMensaje("Mensaje enviado correctamente al channel " + data["channel"]))
    else:
        return jsonify('{"mensaje": "ESTE ENDPOINT ESPERA POST"}')


def returnMensaje(msg):
    return "{{ 'mensaje': {0} }}".format(msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0')