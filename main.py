from responder_api_handler import ResponderClient
import os
from dotenv import load_dotenv
import json

load_dotenv()
c_key = os.getenv("CLIENT_KEY")
c_secret = os.getenv("CLIENT_SECRET")
u_key = os.getenv("USER_KEY")
u_secret = os.getenv("USER_SECRET")
client = ResponderClient(c_key, c_secret, u_key, u_secret)

content = client.get_lists()
if (content is None):
    print('no respone')
with open('.tmp', 'w', encoding='utf8') as f:
    f.write(json.dumps(content, indent=2, ensure_ascii=False))
