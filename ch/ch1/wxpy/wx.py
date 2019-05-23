#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import requests
import json
import re
from wxpy import *

sys.path.append("plugIn")
sys.path.append("helper")
from notice import Notice
from cmbtracker import CmbTracker
from session import Session
from storyAttachment import StoryAttachment
from citracker import CITracker

bot1 = Bot(cache_path=True)

@bot1.register()
def print_others(msg):
    print(msg)
    if msg.is_at:
        txt = msg.text + ""
        if monitor(msg):
            return
        return auto_reply(txt.replace(u"@小鸡", ""))


# 调用青人客机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    result = json.loads(
                requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + text).content
            )
    return result["content"].replace("{br}", "\r\n")

sz_track = bot1.groups().search(u'招赢通SZ Track')[0]
# 可以把需要的群组加入到groups当中
groups = [sz_track]
print groups

plugIns=[]

def start():
    for plugIn in plugIns:
        plugIn.start()

# 监控并分发消息
def monitor(msg):
    for plugIn in plugIns:
        try:
            if hasattr(plugIn , "monitor"):
                if re.search(plugIn.reg , msg.text, re.I) != None:
                    plugIn.monitor(msg)
                    return True
        except AttributeError as e:
            pass
    return False

if __name__ == "__main__":
    # 新开发的组件，继续往该数组当中加，
    # 新组件的启动函数统一为start
    # 新组件的监控函数统一为monitor，组件匹配消息的正则表达式为reg，该方法参数为msg文本
    plugIns.extend([CmbTracker(groups), Notice(groups), Session(groups), StoryAttachment(),  CITracker(groups)])
    start()
    embed()
