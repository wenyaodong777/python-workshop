#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import datetime
from threading import Timer
import sys
sys.path.append("helper")
from formatHelper import Formatter
from restHelper import RestTemplate
from sendHelper import WXSender

class CmbTracker():

    def __init__(self, groups):
        self.groups = groups
        self.itemList = []
        self.formatter = Formatter()
        self.restTemplate = RestTemplate()
        self.sender = WXSender()
        
        self.storyApi = "http://tracker.paas.cmbchina.cn/tracker/busibness/getIterationTrackerWorkitem?iterationUuid=_H7EJwFTpEemRcMv3B5mMZQ&pblId="
        self.bugApi = "http://tracker.paas.cmbchina.cn/tracker/busibness/getWiDefect?filedAgainst=LR15.02%25E6%258B%259B%25E8%25B5%25A2%25E9%2580%259A%25E6%25B8%25A0%25E9%2581%2593&fromDate=undefined&plannedFor=20190401_%25E8%25BF%25AD%25E4%25BB%25A3--R19C04&toDate=undefined"
        
        self.storyContentTemplate = u'[温馨提示] %s建卡啦！\n' \
                            + u'创建时间：%s\n' \
                            + u'故事卡号：%s\n' \
                            + u'简要概述：%s\n' 

        self.bugContentTemplate = u'[温馨提示] %s提单啦！\n' \
                        + u'提单时间：%s\n' \
                        + u'问题单号：%s\n' \
                        + u'简要概述：%s\n' 


    def start(self):
        # self.groups = groups
        Timer(5, self.monitor).start()

    def monitor(self):
        # self.sender.send(self.groups , 'test')
        # Story
        response = self.restTemplate.postCmbTracker(self.storyApi)
        self.handleData(json.loads(response.content)["content"]["itemList"], "story")

        # Bug
        response = self.restTemplate.postCmbTracker(self.bugApi)
        self.handleData(json.loads(response.content)["list"], "bug")

        Timer(5, self.monitor, ).start()

    def handleData(self, itemList, type):
        # 将检索到的故事卡/问题单进行分析
        for item in itemList:
            d = datetime.datetime.strptime(item["creationDate"].replace(".0", ""), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(minutes=120)
            workitemId = item["workitemId"]

            if d > datetime.datetime.now() and workitemId not in self.itemList:
                self.sender.send(self.groups, self.formatItem(item, type))
                self.itemList.append(workitemId)


    def formatItem(self, item, type):
        content = (self.storyContentTemplate if type == 'story' else self.bugContentTemplate) % (item["createdBy"],  item["creationDate"].replace(".0", ""), item["workitemId"],item["summary"])

        # 如果没有写AC则显示描述：
        if type == 'story' :
            if len(item["acceptTest"].strip()):
                content = content + u'验收标准：' + self.formatter.formatStr(item["acceptTest"])
            else:
                content = content + u'详细描述：' + self.formatter.formatStr(item["description"])
        
        return content
