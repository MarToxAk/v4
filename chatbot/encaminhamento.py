from pprint import pprint
from .utils import post_facebook_message
list_oi = ['Ola', 'oi', 'Oi', 'OI', 'oI']
def test(incoming_message):
    for entry in incoming_message['entry']:
        for message in entry['messaging']:
            pprint(message)

            pprint(message['message']['text'])
            for oi in list_oi:
                if oi in message['message']['text']:
                    post_facebook_message(message['sender']['id'])
                else:
                    pprint("Erro")
                    pass