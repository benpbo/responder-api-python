import json
import requests
from string import Template
from OAuth import OAuth

class ResponderClient:
    lists_url_template = Template('http://api.responder.co.il/main/lists/$listId')
    messages_url_template = Template('http://api.responder.co.il/main/lists/$listId/messages/$messageId/')
    views_url_template = Template('http://api.responder.co.il/main/lists/$listId/views/')

    def __init__(self, c_key, c_secret, u_key, u_secret):
        self.oauth = OAuth(c_key, c_secret, u_key, u_secret)
        self.auth_header = self.oauth.generate_auth_header

    def get_lists(self):
        url = ResponderClient.lists_url_template.substitute(listId='')
        res = self.oauth.make_request(url)
        return res.content

    def create_list(self, data):
        url = ResponderClient.lists_url_template.substitute(listId='')
        res = self.oauth.make_request(url, method='POST', data=data)
        return res.content
    
    def update_list(self, list_id, data):
        url = ResponderClient.lists_url_template.substitute(listId=list_id)
        res = self.oauth.make_request(url, method='PUT', data=data)
        return res.content

    def delete_list(self, list_id):
        url = ResponderClient.lists_url_template.substitute(listId=list_id)
        res = self.oauth.make_request(url, method='DELETE')
        return res.content

    def get_messages(self, list_id, message_id=''):
        url = ResponderClient.messages_url_template.substitute(listId=list_id, messageId=message_id)
        res = self.oauth.make_request(url)
        return res.content

    def get_views(self, list_id):
        url = ResponderClient.views_url_template.substitute(listId=list_id)
        res = self.oauth.make_request(url)
        return res.content
