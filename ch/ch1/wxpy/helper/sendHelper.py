#!/usr/bin/python
# -*- coding: UTF-8 -*-
class WXSender():

    def send(self, groups, content):
        for group in groups:
            group.send(content)