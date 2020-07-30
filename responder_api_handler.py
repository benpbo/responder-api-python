import json
import requests
from string import Template
from OAuth import OAuth

class ResponderClient:
    lists_url = 'http://api.responder.co.il/main/lists/'
    messages_url_template = Template('http://api.responder.co.il/main/lists/$listId/messages/$messageId/')
    views_url_template = Template('http://api.responder.co.il/main/lists/$listId/views/')

    def __init__(self, c_key, c_secret, u_key, u_secret):
        self.auth_header = OAuth(c_key, c_secret, u_key, u_secret).generate_auth_header

    def get_lists(self):
        res = requests.get(ResponderClient.lists_url, headers=self.auth_header())
        return res.content

    def create_list(self, data):
        res = requests.post(ResponderClient.lists_url, data=f'info={json.dumps(data)}', headers=self.auth_header())
        return res.content
    
    def update_list(self, list_id, data):
        url = ResponderClient.lists_url + str(list_id)
        res = requests.put(url, data=f'info={json.dumps(data)}', headers=self.auth_header())
        return res.content

    def delete_list(self, list_id):
        url = ResponderClient.lists_url + str(list_id)
        res = requests.delete(url, headers=self.auth_header())
        return res.content

    def get_messages(self, list_id, message_id=''):
        url = ResponderClient.messages_url_template.substitute(listId=list_id, messageId=message_id)
        res = requests.get(url, headers=self.auth_header())
        return res.content

    def get_views(self, list_id):
        url = ResponderClient.views_url_template.substitute(listId=list_id)
        res = requests.get(url, headers=self.auth_header())
        return res.content
