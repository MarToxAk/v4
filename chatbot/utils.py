import json
import requests
from django.conf import settings
from pprint import pprint


def post_facebook_message(fbid):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN2)
    teste = json.dumps({"recipient": {"id": fbid},
                        "messaging_type": "RESPONSE",
                        "message": {
                            "text": "*BOT ILHA BABY*:Bem-Vindo a ILHA BABY. Responda com uma das opções abaixo.",
                            "quick_replies":[
                            {
                                "content_type": "text",
                                "title": "Quero Comprar",
                                "payload": "<POSTBACK_PAYLOAD>",
                                "image_url": "https://cdn.icon-icons.com/icons2/67/PNG/512/shoppingcart_compra_13339.png"
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
