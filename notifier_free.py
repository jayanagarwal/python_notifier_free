import requests
import json

def pushbullet_message(title, body):
    msg = {"type":"note", "title":title, "body":body}
    token = #Enter your API Token here from Pushbullet -> Settings -> API Token
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(msg),
                         headers={'Authorization':'Bearer '+token, "Content-Type":"application/json"})
    if resp.status_code != 200:
        raise Exception('Error',resp.status_code)

    else:
        print('Message Sent!')

subject = input("Enter the Title: ")
message = input("Enter the Message: ")
pushbullet_message(subject,message)