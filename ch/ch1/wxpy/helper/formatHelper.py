#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Formatter():

    def formatStr(self, txt):
        txt = txt.replace("&lt;p&gt;", "")
        txt = txt.replace("&lt;/p&gt;", "")
        txt = txt.replace("&lt;br&gt;", "\n")
        txt = txt.replace("&nbsp;", "")
        txt = txt.replace("<br/>", "")
        return txt
