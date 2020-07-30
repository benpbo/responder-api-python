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

data = client.delete_list(790269)
try:
    json = json.dumps(json.loads(data), indent=2, ensure_ascii=False)
    print(json)
except:
    print(data)
