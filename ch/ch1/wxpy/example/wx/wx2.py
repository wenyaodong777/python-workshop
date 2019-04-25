#!/usr/bin/python
# -*- coding: UTF-8 -*-
from wxpy import *

bot = Bot(True)
my_friend = bot.friends().search(u'隐形的稻草人')
print(my_friend)


@bot.register()
def print_others(msg):
    txt = msg.text
    print(msg)

    txt = txt.replace(u'吗', '')
    txt = txt.replace(u'么', '')
    txt = txt.replace('?',  '!')
    txt = txt.replace(u'？', '!')
    print(txt)
    if msg.text == 'ci':
        return 'ci is ok!'
    # if isinstance(msg.chat, Group) and not msg.is_at:
    #    return txt
    # else:
    #    return 'hello'
    return txt


@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)


embed()
