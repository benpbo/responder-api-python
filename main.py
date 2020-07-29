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
    'info': {
        'DESCRIPTION': 'test'
    }
}
print(client.create_list({}))
content = client.get_lists()
