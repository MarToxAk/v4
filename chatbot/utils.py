import json
import requests
from django.conf import settings
from pprint import pprint


def post_facebook_message(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    teste = json.dumps({"recipient": {"id": fbid},
                        "message": {
                            "attachment": {
                                "type": "template",
                                "payload": {
                                    "template_type": "open_graph",
                                    "elements": [
                                        {
                                            "url": "https://open.spotify.com/track/7GhIk7Il098yCjg4BQjzvb",
                                            "buttons": [
                                                {
                                                    "type": "web_url",
                                                    "url": "https://en.wikipedia.org/wiki/Rickrolling",
                                                    "title": "View More"
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
