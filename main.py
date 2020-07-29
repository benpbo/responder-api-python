import requests
import urllib.parse as url_parser
from hashlib import md5
from dotenv import load_dotenv
import os
import time
from uuid import uuid4
import json

def generate_nonce():
    return uuid4().hex

def generate_timestamp():
    return int(time.time())

load_dotenv()
c_key = os.getenv("CLIENT_KEY")
c_secret = os.getenv("CLIENT_SECRET")
u_key = os.getenv("USER_KEY")
u_secret = os.getenv("USER_SECRET")
nonce = generate_nonce()
timestamp = generate_timestamp()

url = 'http://api.responder.co.il/main/lists'
headers = {
    'Authorization': f'c_key={c_key},c_secret={md5((c_secret+nonce).encode()).hexdigest()},u_key={u_key},u_secret={md5((u_secret+nonce).encode()).hexdigest()},nonce={nonce},timestamp={timestamp}'
}
res = requests.get(url, headers=headers)
content = json.loads(res.content)
with open('.tmp', 'w', encoding='utf8') as f:
    f.write(json.dumps(content, indent=2, ensure_ascii=False))
