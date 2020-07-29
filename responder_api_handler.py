from hashlib import md5
from dotenv import load_dotenv
import os
import time
from uuid import uuid4
import json
import requests
from string import Template


class OAuth:
    def __init__(self, c_key, c_secret, u_key, u_secret):
        self.c_key = c_key
        self.c_secret = c_secret
        self.u_key = u_key
        self.u_secret = u_secret

    def generate_auth_header(self):
        nonce = self.generate_nonce()
        timestamp = self.generate_timestamp()
        return {
            'Authorization': f'c_key={self.c_key},c_secret={md5((self.c_secret+nonce).encode()).hexdigest()},u_key={self.u_key},u_secret={md5((self.u_secret+nonce).encode()).hexdigest()},nonce={nonce},timestamp={timestamp}'
        }

    @staticmethod
    def generate_nonce():
        return uuid4().hex

    @staticmethod
    def generate_timestamp():
        return int(time.time())


class ResponderClient:
    lists_url = 'http://api.responder.co.il/main/lists'
    messages_url_template = Template('http://api.responder.co.il/main/lists/$listId/messages/$messageId')
    views_url_template = Template('http://api.responder.co.il/main/lists/$listId/views')

    def __init__(self, c_key, c_secret, u_key, u_secret):
        self.oauth = OAuth(c_key, c_secret, u_key, u_secret)
        self.auth_header = self.oauth.generate_auth_header

    def get_lists(self):
        res = requests.get(ResponderClient.lists_url, headers=self.auth_header())
        return json.loads(res.content)

    def get_messages(self, list_id, message_id=''):
        url = ResponderClient.messages_url_template.substitute(listId=list_id, messageId=message_id)
        res = requests.get(url, headers=self.auth_header())
        return json.loads(res.content)

    def get_views(self, list_id):
        url = ResponderClient.views_url_template.substitute(listId=list_id)
        res = requests.get(url, headers=self.auth_header())
        return json.loads(res.content)
