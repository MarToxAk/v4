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
                                "template_type": "airline_boardingpass",
                                "intro_message": "You are checked in.",
                                "locale": "en_US",
                                "boarding_pass": [
                                  {
                                    "passenger_name": "SMITH\/NICOLAS",
                                    "pnr_number": "CG4X7U",
                                    "seat": "74J",
                                    "logo_image_url": "https:\/\/www.example.com\/en\/logo.png",
                                    "header_image_url": "https:\/\/www.example.com\/en\/fb\/header.png",
                                    "qr_code": "M1SMITH\/NICOLAS  CG4X7U nawouehgawgnapwi3jfa0wfh",
                                    "above_bar_code_image_url": "https:\/\/www.example.com\/en\/PLAT.png",
                                    "auxiliary_fields": [
                                      {
                                        "label": "Terminal",
                                        "value": "T1"
                                      },
                                      {
                                        "label": "Departure",
                                        "value": "30OCT 19:05"
                                      }
                                    ],
                                    "secondary_fields": [
                                      {
                                        "label": "Boarding",
                                        "value": "18:30"
                                      },
                                      {
                                        "label": "Gate",
                                        "value": "D57"
                                      },
                                      {
                                        "label": "Seat",
                                        "value": "74J"
                                      },
                                      {
                                        "label": "Sec.Nr.",
                                        "value": "003"
                                      }
                                    ],
                                    "flight_info": {
                                      "flight_number": "KL0642",
                                      "departure_airport": {
                                        "airport_code": "JFK",
                                        "city": "New York",
                                        "terminal": "T1",
                                        "gate": "D57"
                                      },
                                      "arrival_airport": {
                                        "airport_code": "AMS",
                                        "city": "Amsterdam"
                                      },
                                      "flight_schedule": {
                                        "departure_time": "2016-01-02T19:05",
                                        "arrival_time": "2016-01-05T17:30"
                                      }
                                    }
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
