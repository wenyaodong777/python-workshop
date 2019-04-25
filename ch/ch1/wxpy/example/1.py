#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jenkins
from wxpy import *

import aiml
import os

bot1 = Bot()
my_friend = bot1.friends().search(u'隐形的稻草人')
print(my_friend)

os.chdir('./src/alice')
alice = aiml.Kernel();
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

print alice.respond('hi');

@bot1.register()
def print_others(msg):
    txt = msg.text;
    print(msg)
    txt = txt.replace(u'吗', '')
    txt = txt.replace(u'么', '')
    txt = txt.replace('?',  '!')
    txt = txt.replace(u'？', '!')
    return alice.respond(txt)


    

# print 111
# @bot1.register(my_friend)
# def reply_my_friend(msg):
#     return 'received: {} ({})'.format(msg.text, msg.type)

embed();