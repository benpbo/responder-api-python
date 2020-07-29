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

content = client.get_lists()

lists = [lst['ID'] for lst in content['LISTS']]
views = [client.get_views(list_id) for list_id in lists]

with open('.tmp', 'w', encoding='utf8') as f:
    f.write(json.dumps(views, ensure_ascii=False, indent=2))
