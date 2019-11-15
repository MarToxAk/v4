import json
import requests
from django.conf import settings
from pprint import pprint


def post_facebook_message(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    teste = json.dumps({"recipient": {"id": fbid},
                        "messaging_type": "RESPONSE",
                        "message": {
                            "text": "Pick a color:",
                            "quick_replies": [
                                {
                                    "content_type": "text",
                                    "title": "Red",
                                    "payload": "<POSTBACK_PAYLOAD>",
                                    "image_url": "http://example.com/img/red.png"
                                }, {
                                    "content_type": "text",
                                    "title": "Green",
                                    "payload": "<POSTBACK_PAYLOAD>",
                                    "image_url": "http://example.com/img/green.png"
                                }
                            ]
                        }
                        }
                       )
    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=teste)
    pprint(status.json())
