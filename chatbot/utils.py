import json
import requests
from django.conf import settings
from pprint import pprint


def post_facebook_message(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    response_msg = json.dumps({"recipient": {"id": fbid},
                               "message": {"text": f'1{recevied_message}'}})
    teste = json.dumps({"recipient": {"id": fbid},
                        "message": {
                            "attachment": {
                                "type": "template",
                                "payload": {
                                    "template_type": "button",
                                    "text": "What do you want to do next?",
                                    "buttons": [
                                        {
                                            "type": "phone_number",
                                            "url": "+5512996745251",
                                            "title": "Ligue para Gente"
                                        },
                                    ]
                                }
                            }
                        }
                        }
                       )
    status = requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=teste)
    pprint(status.json())