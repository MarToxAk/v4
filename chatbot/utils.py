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
                                    "text": "Try the postback button!",
                                    "persistent_menu": [
                                        {
                                            "locale": "default",
                                            "composer_input_disabled": false,
                                            "call_to_actions": [
                                                {
                                                    "type": "postback",
                                                    "title": "Talk to an agent",
                                                    "payload": "CARE_HELP"
                                                },
                                                {
                                                    "type": "postback",
                                                    "title": "Outfit suggestions",
                                                    "payload": "CURATION"
                                                },
                                                {
                                                    "type": "web_url",
                                                    "title": "Shop now",
                                                    "url": "https://www.originalcoastclothing.com/",
                                                    "webview_height_ratio": "full"
                                                }
                                            ]
                                        }
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