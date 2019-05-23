#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sendHelper import WXSender
from jenkinsHelper import JenkinsServer

class CITracker():
    def __init__(self, groups):
        self.groups = groups
        self.sender = WXSender()
        self.jenkinsServer = JenkinsServer()
        self.reg = 'ci'
        print 'CI!!!!!!!!!!!!!!!!!!!!'

    def start(self):
        print 'CI tracker'
        return

    def monitor(self, msg):
        replyInfo = u''
        jobs = self.jenkinsServer.jenkinsInit()._get_view_jobs("current_iteration")
        infos = []
        for job in jobs:
            infos.append(job["fullname"] + "(" + job["color"] + ")")

        for info in infos:
            print info
            replyInfo += info + '\n'

        print replyInfo
        self.sender.send(self.groups, u'CI状态：\n'+replyInfo)