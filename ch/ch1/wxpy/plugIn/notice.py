#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import time
import schedule
import sys
sys.path.append("helper")
from sendHelper import WXSender

class Notice():

    def __init__(self, groups):
        self.groups = groups
        self.sender = WXSender();

    def checkIn(self):
        self.sender.send(self.groups, u"【签到提醒】小哥哥，小姐姐们，上班第一件事就是签到哟，可别忘记了！")
    
    def checkOut(self):
        self.sender.send(self.groups, u"【签退提醒】小哥哥，小姐姐们，辛苦了一天，下班记得签到哟，小鸡一直陪伴着您！")

    def timecard(self):
        self.sender.send(self.groups, u"【报公/Timecard提醒】小哥哥，小姐姐们，今天周五要报公/填Timecard啦！")

    def start(self):
        schedule.every().day.at('08:20').do(self.checkIn)
        schedule.every().day.at('18:00').do(self.checkOut)    
        schedule.every().friday.at('11:42').do(self.timecard)

# print datetime.datetime.now().weekday()
# print datetime.date(2019, 4 , 1).weekday()
# print datetime.date(2019, 4 , 7).weekday()
