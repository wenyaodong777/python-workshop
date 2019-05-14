#!/usr/bin/python
# -*- coding: UTF-8 -*-
from wxpy import *
import requests
import json

# 机器人对象
bot = Bot(cache_path=True,console_qr=True)

# 抓到某个聊天群组
workshop=bot.groups().search(u'Workshop 额靠重意雷')[0];

workshop.send("test");

# @bot.register(workshop)
# def print_msg(msg):
#     print msg;
#     return auto_reply(msg.text)

# def speak(text):
#     url = "http://www.tuling123.com/openapi/api/v2"
#     payload = {
#         "reqType": 0,
#         "userInfo": {
#             "apiKey": "4fbaee034f0846f29d7ba95be73ef3b5",
#             "userId": "407506"
#         },
#         "perception": {
#             "inputText": {
#                 "text": text
#             }
#         }
#     }
#     r = requests.post(url, data=json.dumps(payload))
#     message = json.loads(r.content)["results"][0]["values"]["text"];
#     return message

# def auto_reply(text):
#     response = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + text);

#     message = json.loads(response.content)["content"];
#     print message;
#     return message;



embed()
