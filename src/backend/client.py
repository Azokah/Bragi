import requests, json

TOKEN = 'xoxp-481750559073-483405870279-481624017200-7558321bf81b138192a14bc38e5c34cb'

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
    print(msg)
    print(channel_id)
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
    print(response.text)
    return ''


def user_list():
    url = 'https://slack.com/api/users.list'

    headers = {
        'cache-control': "no-cache",
        'authorization': "Bearer " + TOKEN
        }

    response = requests.request("GET", url, headers=headers)
    resp = json.loads(response.text)
    print(resp)
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
    
    print(response.text)
    return ''


 
# print(create_channel("tercera"))
# print(list_channel())

# print(create_channel("Un_canal"))

#msg = input("mensaje:")
#print(send_msg(msg, 'CDDJ5MQRG'))


#users = []
#for u in user_list():
#    users.append(u['id'])


# print(direct_msg(','.join(users)))
# print(conversation_open('UDCRPEG2C,UDD02VA5P,UDD032KC1,UDD03SZMX,UDEKKML7R,UDEKLSBKR'))

# print(send_msg("Hola Gente", "GDDJGBPEW"))
# print(user_list())
