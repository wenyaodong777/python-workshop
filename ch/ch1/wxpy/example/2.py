#!/usr/bin/python
# -*- coding: UTF-8 -*-
from wxpy import *
import json
import requests

bot1 = Bot(console_qr=True, cache_path=True)
my_friend = bot1.friends().search(u'隐形的稻草人')
print(my_friend)


@bot1.register()
def print_others(msg):
    txt = msg.text;
    print msg;
    return auto_reply(txt)


# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api/v2"
    payload = {
        "reqType": 0,
        "userInfo": {
            "apiKey": "427459373fa54b179a9d560ff5d6f348",
            "userId": "407506"
        },
        "perception": {
            "inputText": {
                "text": text
            }
        }
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return result["results"][0]["values"]["text"];


embed();
