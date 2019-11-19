import json
import requests
from django.conf import settings
from pprint import pprint


def post_facebook_message(fbid, first_name):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    teste = json.dumps({"recipient": {"id": fbid},
                        "messaging_type": "RESPONSE",
                        "message": {
                            "text": f"*BOT ILHA BABY*: Bem-Vindo {first_name} a ILHA BABY. Ecolha uma das opções abaixo.",
                            "quick_replies":[
                            {
                                "content_type": "text",
                                "title": "Quero Comprar",
                                "payload": "comprar",
                                "image_url": "https://cdn.icon-icons.com/icons2/67/PNG/512/shoppingcart_compra_13339.png"
                            }, {
                                "content_type": "text",
                                "title": "Sair",
                                "payload": "sair",
                                "image_url": "https://cdn3.iconfinder.com/data/icons/interface/100/close_button_2-512.png"
                            }
                        ]
                        }
                        }
                       )
    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=teste)
    pprint(status.json())
def post_facebook_message_sair(fbid, first_name):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    teste = json.dumps({"recipient": {"id": fbid},
                        "message": {
                            "text": f"*BOT ILHA BABY*: Obrigado pela Atenção {first_name}.",                      }
                        }
                       )
    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=teste)
    pprint(status.json())