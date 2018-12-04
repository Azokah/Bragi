from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS, cross_origin
import json, client
import oauth2
import json
import urllib
import twconfig

from client import send_msg

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
    data['getMessagesFromChannel'] = '[{"msg":"POST, devuelve los mensajes de un channel", "param-1": "channel"}]'
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
    elif request.method == 'GET':
        return jsonify('{"mensaje": "ESTE ENDPOINT ESPERA POST"}')
    else:
        return jsonify('{"mensaje": "MENSAJE NO RECONOCIDO"}')

@app.route('/slack/getMessagesFromChannel', methods=['POST'])
def slackGetMessagesFromChannel():
    data = request.get_json(force=True)
    return jsonify(client.conversation_history(data['channel']))


def returnMensaje(msg):
    return "{{ 'mensaje': {0} }}".format(msg)


# TWITTER

CONSUMER_KEY = twconfig.SECRET_CONSUMER_KEY
CONSUMER_SECRET = twconfig.SECRET_CONSUMER_SECRET

ACCESS_TOKEN = twconfig.SECRET_ACCESS_TOKEN
ACCESS_TOKEN_SECRET = twconfig.SECRET_ACCESS_TOKEN_SECRET

def oauth_req(url, key, secret, http_method="GET", post_body=b"", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers )
    return content, resp

def json_str(json_obj):
    return json.dumps(json_obj, indent=2, sort_keys=True)

def get_timeline():
    home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/home_timeline.json', ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    data = home_timeline[0].decode('utf-8', 'replace')
    obj = json.loads(data)

    msjs = []

    for m in obj:
        msjs.append({ 'mensaje': m["text"], 'user': m['user']['name'] })

    return jsonify(msjs)

def post_tweet(tweet):
    params = urllib.parse.urlencode({ 'status': tweet })
    home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/update.json?' + params, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, http_method='POST')
    data = home_timeline[0].decode('utf-8', 'replace')
    obj = json.loads(data)
    return str(obj['id'])

@app.route('/twitter/get_timeline', methods=['GET'])
def getTimeline():
    timeline = get_timeline()
    return timeline
    
@app.route('/twitter/post_tweet', methods=['POST'])
def postTweet():
    data = request.get_json(force=True)
    return post_tweet(data["mensaje"])

if __name__ == '__main__':
    app.run(host='0.0.0.0')