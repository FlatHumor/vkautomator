# coding=utf-8

from __future__ import unicode_literals

import requests
import json



class Session(object):

    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.vk.com/method/"
        self.api_version = "5.68"

    def __getattr__(self, method):
        return VkRequest(self, method)


class VkRequest(object):

    def __init__(self, session, method_name):
        self._session = session
        self._method_name = method_name
        self._method_kwargs = dict()

    def __getattr__(self, method):
        return VkRequest(self._session, self._method_name + '.' + method)

    def send_request(self):
        url = self._session.base_url + self._method_name
        self._method_kwargs['access_token'] = self._session.token
        self._method_kwargs['v'] = self._session.api_version
        response = requests.get(url, self._method_kwargs)
        return VkResponse(response.text)

    def __call__(self, **kwargs):
        self._method_kwargs.update(kwargs)
        return self.send_request()


class VkResponse(object):

    def __init__(self, response_text):
        self._response_text = response_text
        self.response = None

    def parse_response_text(self):
        response_dict = json.loads(self._response_text)
        self.response = response_dict.get("response", None)

    @property
    def total_items(self):
        return self.response.get("count", None)

    @property
    def last_message_id(self):
        return self.response['items'][0]['id']

    @property
    def last_message_text(self):
        return self.response['items'][0]['body']

    @property
    def last_message_sender(self):
        return self.response['items'][0]['from_id']

    def get_items(self):
        if isinstance(self.response, dict):
            items = self.response.get("items", 0)
            return [VkItem(item) for item in items]
        elif isinstance(self.response, list):
            return [VkItem(item) for item in self.response]


class VkItem(object):
    def __init__(self, item):
        self.__dict__.update(item)
