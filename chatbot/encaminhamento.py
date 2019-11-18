from pprint import pprint
from .utils import post_facebook_message

def test(incoming_message):
    for entry in incoming_message['entry']:
        for message in entry['messaging']:
            pprint(message)
            pprint(message['message']['text'])
            if 'oi' in message['message']['text']:
                post_facebook_message(message['sender']['id'])
            else:
                pass