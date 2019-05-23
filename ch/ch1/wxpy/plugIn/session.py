#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import json
import dateutil.parser
from datetime import datetime
from restHelper import RestTemplate
from sendHelper import WXSender


class Session:

    def __init__(self, groups):
        self.restTemplate = RestTemplate()
        self.sessionApi = 'https://api.trello.com/1'
        self.groups = groups
        self.reg = 'session'
        self.sender = WXSender()

    def start(self):
        print 'start session bot'
        return

    def monitor(self, msg):
        print msg.text
        if re.search('session-list$', msg.text):
            self.handle_sessions()
        elif re.search('session-apply', msg.text):
            self.apply_session(msg)
        else:
            print 'session not support'
            self.sender.send(self.groups, u'支持指令格式：\n 1. session-list \n 2. session-apply-名称-时间')
        return

    def handle_sessions(self):
        print 'start get sessions'
        cards = self.get_sessions()
        print 'get session success'
        response = u''
        for card in cards:
            response = response + u'名字：%s, 时间：%s \n' % (
                card['name'], dateutil.parser.parse(card['due']).strftime('%Y-%m-%d'))
        print response
        return self.sender.send(self.groups, response)

    def apply_session(self, msg):
        print 'start apply session'
        msgFormat = re.search('session-apply-(\S+)-(\S+)', msg.text)
        print msgFormat
        try:
            name = msgFormat.group(1)
            date = datetime.strptime(msgFormat.group(2), '%Y%m%d').strftime('%Y-%m-%d')
            sender = msg.member
            print date
            card = self.apply_sessions(name, date, sender)
            self.sender.send(self.groups, u'报名成功, 如需修改请去' + card['url'])
        except Exception as e:
            print e.message
            self.sender.send(self.groups, u'报名失败，请输入正确格式session-apply-名字-时间(YYYYMMDD)')
        return

    def get_sessions(self):
        response = self.restTemplate.getSessions(self.sessionApi + '/boards/Eq8vtFTB/cards')
        print response
        return json.loads(response.content)

    def apply_sessions(self, name, date, sender):
        print 'start response'
        response = self.restTemplate.applySessions(self.sessionApi + '/cards', name, date, sender)
        print response.content
        return json.loads(response.content)
