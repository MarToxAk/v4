import json
import requests
from django.conf import settings
from pprint import pprint


def post_facebook_message(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.ACCESS_TOKEN)
    teste = json.dumps({"recipient": {"id": fbid},
                        "message":{
                            "attachment":{
                              "type":"template",
                              "payload":{
                                "template_type":"generic",
                                "elements":[
                                   {
                                    "title":"Welcome!",
                                    "image_url":"https://petersfancybrownhats.com/company_image.png",
                                    "subtitle":"We have the right hat for everyone.",
                                    "default_action": {
                                      "type": "web_url",
                                      "url": "https://petersfancybrownhats.com/view?item=103",
                                      "messenger_extensions": false,
                                      "webview_height_ratio": "tall",
                                      "fallback_url": "https://petersfancybrownhats.com/"
                                    },
                                    "buttons":[
                                      {
                                        "type":"web_url",
                                        "url":"https://petersfancybrownhats.com",
                                        "title":"View Website"
                                      },{
                                        "type":"postback",
                                        "title":"Start Chatting",
                                        "payload":"DEVELOPER_DEFINED_PAYLOAD"
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
