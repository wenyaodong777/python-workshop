# -*- coding: utf-8 -*-
# coding=utf-8
# encoding: utf-8
from wxpy import *

bot = Bot();
my_friend = bot.friends().search('\u9690\u5f62\u7684\u7a3b\u8349\u4eba')
print(my_friend);