#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import requests
import json
from wxpy import *

sys.path.append("plugIn")
sys.path.append("helper")
from notice import Notice
from cmbtracker import CmbTracker

bot1 = Bot(console_qr=True, cache_path=True)

@bot1.register()
def print_others(msg):
    print (msg)
    if msg.is_at:
        txt = msg.text + ""
        return auto_reply(txt.replace(u"@小鸡", ""))


# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    print (text)
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + text
    r = requests.get(url)
    result = json.loads(r.content)
    print(result)
    return result["content"].replace("{br}", "\r\n")


sz_track = bot1.groups().search(u'招赢通Test Track')[0]
groups = [sz_track]

if __name__ == "__main__":
    CmbTracker(groups).start()
    Notice(groups).start();
    embed()
