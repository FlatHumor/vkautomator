# coding=utf-8

from .session import Session


class LittleClient(object):

    def __init__(self, token):
        self._receiver_id = 740528
        self._selderey_id = 474977830
        self._sender_id = 474977830
        self._last_message_id = 0
        self._token = token

    def get_new_message(self):
        session = Session(self._token)
        response = session.messages.getHistory(user_id=self._receiver_id, count=1)
        response.parse_response_text()
        if int(response.last_message_sender) == self._selderey_id:
            return
        if int(response.last_message_id) != self._last_message_id:
            print("received message: %s" % response.last_message_text)
            # self.answer_to_message(response.last_message_text)
            self._last_message_id = int(response.last_message_id)
            self._receiver_id = int(response.last_message_sender)
            return response.last_message_text

