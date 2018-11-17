import requests, json

TOKEN = 'xoxp-481750559073-483405870279-482200241012-04f62848d200fd3a578414738ed36b8e'

def create_conversations(name):
    url = "https://slack.com/api/conversations.create"

    querystring = {"name":name}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'authorization': "Bearer " + TOKEN
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    resp = json.loads(response.text)
    if resp['ok']:
        return resp['channel']['id']

    return ''

def list_channel():
    url = "https://slack.com/api/conversations.list"

    headers = {
        'cache-control': "no-cache",
        'authorization': "Bearer " + TOKEN
        }

    response = requests.request("GET", url, headers=headers)
    resp = json.loads(response.text)
    channels = []
    for c in resp['channels']:
        channels.append({'id': c['id'], 'name': c['name']})

    return channels


def send_msg(msg, channel_id):
    url = "https://slack.com/api/chat.postMessage"
    payload = "'text': '{}', 'channel': '{}'".format(msg, channel_id)
    payload = '{' + payload  + '}'
 
    headers = {
        'cache-control': "no-cache",
        'authorization': "Bearer " + TOKEN,
        'Content-Type': 'application/json'
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    resp = json.loads(response.text)

    return resp['ok']
    
# Deprecated, usar conversations
def create_channel(name):
    url = "https://slack.com/api/channels.create"

    querystring = {"name":name}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'authorization': "Bearer " + TOKEN
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    resp = json.loads(response.text)
    if resp['ok']:
        return resp['channel']['id']
    return ''


def user_list():
    url = 'https://slack.com/api/users.list'

    headers = {
        'cache-control': "no-cache",
        'authorization': "Bearer " + TOKEN
        }

    response = requests.request("GET", url, headers=headers)
    resp = json.loads(response.text)
    users = []
    for c in resp['members']:
        users.append({'id': c['id'], 'team_id': c['team_id'], 'name': c['name'], 'real_name': c['real_name']})

    return users

def conversation_open(users):
    url = "https://slack.com/api/conversations.open"

    payload = "'users': '{}'".format(users)
    payload = '{' + payload  + '}'

    headers = {
        'cache-control': "no-cache",
        'authorization': "Bearer " + TOKEN,
        'Content-Type': 'application/json;charset=utf-8'
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    resp = json.loads(response.text)
    if resp['ok']:
        return resp['channel']['id']
    
    return ''

def conversation_history(channel):
    url = 'https://slack.com/api/conversations.history?token=' + TOKEN + '&channel=' + channel

    response = requests.request("POST", url)
    resp = json.loads(response.text)

    if resp['ok']:
        return sorted(resp['messages'], key = lambda i: i['ts']) # resp['messages']
        
    return '{"message": "error"}'