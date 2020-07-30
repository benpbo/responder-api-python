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
    "TYPE": "1",  # 1 for "messer boded", 0 for "sidrat messarim", 2 for "mevusas ta'arich"
    # 0 for regular HTML editor(affects the type of editor used in the website)
    "BODY_TYPE": "0",
    "SUBJECT": 'message subject2',
    "BODY": 'message HTML body',
    "FILTER": "",  # -optional - the view id "kvuzat mishloah"
    'LANGUAGE': "hebrew",  # -optional - defaults to 'english'
    'CHECK_LINKS': "1"
}
msg_update = {
    'LANGUAGE': 'english'
}

subscribers = [
    {
        "NAME": "John Smith",
        "EMAIL": "johnsmith@gmail.com",
        "DAY": 12,
        # parameter for email's notification for the user about new subscriber. (0 - don't notify / 1 - notify / 2 - according to list's settings)
        "NOTIFY": 2
    },
    {
        "NAME": "Bob Jones",
        "EMAIL": "bobjones@yahoo.com",
        # parameter for email's notification for the user about new subscriber. (0 - don't notify / 1 - notify / 2 - according to list's settings)
        "NOTIFY": 0
    },
    {
        'NAME': 'Ben Prize',
        'EMAIL': 'prizeben@gmail.com'
    }
]
list_id = 0
for lst in json.loads(client.get_lists())['LISTS']:
    if lst['DESCRIPTION'] == 'test':
        list_id = lst['ID']
        break

message_id = 0
for msg in json.loads(client.get_messages(list_id)):
    if msg['SUBJECT'] == 'test message':
        message_id = msg['ID']
        break

email = ''
for subscriber in json.loads(client.get_subscribers(list_id)):
    if subscriber['NAME'] == 'Ben Prize':
        email = subscriber['EMAIL']

msg_test = {
    'email': email
}
data = client.test_message(list_id, message_id, msg_test)

try:
    json = json.dumps(json.loads(data), indent=2, ensure_ascii=False)
    print(json)
except:
    print(data)
