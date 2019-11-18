from pprint import pprint
from .utils import post_facebook_message
import urllib.request
import json
from django.conf import settings

list_oi = ['Ola', 'oi', 'Oi', 'OI', 'oI']


def test(incoming_message):
    for entry in incoming_message['entry']:
        for message in entry['messaging']:
            pprint(message)

            pprint(message['message']['text'])
            for oi in list_oi:
                if oi in message['message']['text']:
                    with urllib.request.urlopen(
                            f"https://graph.facebook.com/{message['sender']['id']}?fields=first_name,last_name,profile_pic&access_token={settings.ACCESS_TOKEN}") as url:
                        first_name = json.loads(url.read().decode('utf-8'))
                        pprint(first_name)
                    post_facebook_message(message['sender']['id'], first_name['first_name'])

                else:
                    pass