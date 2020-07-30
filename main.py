from responder_api_handler import ResponderClient
import os
from dotenv import load_dotenv
import json
import bs4

load_dotenv()
c_key = os.getenv("CLIENT_KEY")
c_secret = os.getenv("CLIENT_SECRET")
u_key = os.getenv("USER_KEY")
u_secret = os.getenv("USER_SECRET")
client = ResponderClient(c_key, c_secret, u_key, u_secret)

lst = {
    'DESCRIPTION': 'test',
    'SENDER_NAME': 'ben',
    'SENDER_EMAIL': 'prizeben@gmail.com',
    'SENDER_ADDRESS': 'somewhere'
}

msg = {
    "TYPE": "1", # 1 for "messer boded", 0 for "sidrat messarim", 2 for "mevusas ta'arich"
    "BODY_TYPE": "0", # 0 for regular HTML editor(affects the type of editor used in the website)
    "SUBJECT": 'message subject2',
    "BODY": 'message HTML body',
    "FILTER": "", # -optional - the view id "kvuzat mishloah"
    'LANGUAGE': "hebrew", # -optional - defaults to 'english'
    'CHECK_LINKS': "1"
}
msg_update = {
    'LANGUAGE': 'english'
}
list_id = 0
for lst in json.loads(client.get_lists())['LISTS']:
    if lst['DESCRIPTION'] == 'test':
        list_id = lst['ID']
        break

#list_id = json.loads(client.create_list(lst))['LIST_ID']
#data = client.create_message(list_id, msg)

message_id = 0
for msg in json.loads(client.get_messages(list_id)):
    if msg['SUBJECT'] == 'test message':
        message_id = msg['ID']
    
data = client.update_message(list_id, message_id, msg_update)
try:
    json = json.dumps(json.loads(data), indent=2, ensure_ascii=False)
    print(json)
except:
    print(data)
