from hashlib import md5
import time
from uuid import uuid4
from requests import request
import json


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

    def make_request(self, url: str, method = 'GET', **kwargs):
        method = method.upper()
        
        if 'data' in kwargs:
            data = kwargs['data']
            return request(method, url, data=f'info={json.dumps(data)}', headers=self.generate_auth_header())
        else: 
            return request(method, url, headers=self.generate_auth_header())

    @staticmethod
    def generate_nonce():
        return uuid4().hex

    @staticmethod
    def generate_timestamp():
        return int(time.time())
