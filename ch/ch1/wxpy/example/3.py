#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "start";

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
    print 456
    if text == u'深圳天气':
        # url = "http://t.weather.sojson.com/api/weather/city/101280601"
        # r = requests.get(url)
        # data = json.loads(r.content)["data"]
        # info = data["forecast"][0]["week"] + "   " + data["forecast"][0]["type"] + u"    " + data["forecast"][0]["ymd"] + u"\r\n" 
        # info = info + u"当前温度: " + data["wendu"] + u" <" + data["forecast"][0]["low"] + u"~" +data["forecast"][0]["high"] + u">\r\n"
        # info = info + u"空气质量: " + data["quality"] + u"\r\n"
        # info = info + u"今日风向: " + data["forecast"][0]["fx"] + u"  等级" + data["forecast"][0]["fl"] + u"\r\n"
        # info = info + u"小鸡愿望: " + data["forecast"][0]["notice"] + u"\r\n";
        # print info;
        # # return info;
        return '123123123';

    # 聊天功能
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + text;
    r = requests.get(url)
    result = json.loads(r.content)
    msg = result["content"]
    print msg
    return result["content"].replace("{br}" , "\r\n")

embed()
