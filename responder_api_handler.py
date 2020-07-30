import json
import requests
from string import Template
from OAuth import OAuth


class ResponderClient:
    lists_url_template = Template(
        'http://api.responder.co.il/main/lists/$listId')
    messages_url_template = Template(
        'http://api.responder.co.il/main/lists/$listId/messages/$messageId/')
    subscribers_url_template = Template(
        'http://api.responder.co.il/main/lists/$listId/subscribers/')
    views_url_template = Template(
        'http://api.responder.co.il/main/lists/$listId/views/')

    def __init__(self, c_key, c_secret, u_key, u_secret):
        self.oauth = OAuth(c_key, c_secret, u_key, u_secret)

    def get_lists(self):
        url = ResponderClient.lists_url_template.substitute(listId='')
        res = self.oauth.make_request(url)
        return res.content

    def create_list(self, data):
        url = ResponderClient.lists_url_template.substitute(listId='')
        res = self.oauth.make_request(url, 'POST', data=data)
        return res.content

    def update_list(self, list_id, data):
        url = ResponderClient.lists_url_template.substitute(listId=list_id)
        res = self.oauth.make_request(url, 'PUT', data=data)
        return res.content

    def delete_list(self, list_id):
        url = ResponderClient.lists_url_template.substitute(listId=list_id)
        res = self.oauth.make_request(url, 'DELETE')
        return res.content

    def get_messages(self, list_id, message_id=''):
        url = ResponderClient.messages_url_template.substitute(
            listId=list_id,
            messageId=message_id
        )
        res = self.oauth.make_request(url)
        return res.content

    def create_message(self, list_id, data):
        url = ResponderClient.messages_url_template.substitute(
            listId=list_id,
            messageId=''
        )
        res = self.oauth.make_request(url, 'POST', data=data)
        return res.content

    def update_message(self, list_id, message_id, data):
        url = ResponderClient.messages_url_template.substitute(
            listId=list_id,
            messageId=message_id
        )
        res = self.oauth.make_request(url, 'PUT', data=data)
        return res.content

    def test_message(self, list_id, message_id, data):
        url = ResponderClient.messages_url_template.substitute(
            listId=list_id,
            messageId=message_id
        )
        res = self.oauth.make_request(url, 'POST', data=data, data_type='data')
        return res.content

    def delete_message(self, list_id, message_id):
        pass

    def get_subscribers(self, list_id): 
        url = ResponderClient.subscribers_url_template.substitute(
            listId=list_id
        )
        res = self.oauth.make_request(url)
        return res.content

    def create_subscribers(self, list_id, data):
        url = ResponderClient.subscribers_url_template.substitute(
            listId=list_id
        )
        res = self.oauth.make_request(url, 'POST', data=data, data_type='subscribers')
        return res.content

    def get_views(self, list_id):
        url = ResponderClient.views_url_template.substitute(listId=list_id)
        res = self.oauth.make_request(url)
        return res.content
