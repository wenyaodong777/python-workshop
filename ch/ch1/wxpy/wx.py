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


# 调用青人客机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    result = json.loads(
                requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + text).content
            )
    return result["content"].replace("{br}", "\r\n")

print bot1.groups()

sz_track = bot1.groups().search(u'招赢通Test Track')[0]
# sz_track = bot1.groups().search(u'123456')[0]
# groups = [sz_track]
groups = bot1.groups().search(u'123456')
print groups

if __name__ == "__main__":
    CmbTracker(groups).start()
    Notice(groups).start();
    embed()
