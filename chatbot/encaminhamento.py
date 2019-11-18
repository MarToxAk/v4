from pprint import pprint
from .utils import post_facebook_message
list_oi = ['Ola', 'oi', 'Oi', 'OI', 'oI']
def test(incoming_message):
    for entry in incoming_message['entry']:
        for message in entry['messaging']:
            pprint(message)

            pprint(message['message']['text'])
            if any(ext in list_oi for ext in message['message']['text']):
                post_facebook_message(message['sender']['id'])
            else:
                pass