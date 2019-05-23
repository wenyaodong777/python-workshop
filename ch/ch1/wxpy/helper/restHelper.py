#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests


class RestTemplate():

    def postCmbTracker(self, url):
        return requests.post(url,
                             headers={
                                 'Accept': 'application/json, text/plain, */*',
                                 'Referer': 'http://devops.paas.cmbchina.cn/',
                                 'Origin': 'http://devops.paas.cmbchina.cn',
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
                             })

    def getSessions(self, url):
        return requests.get(url, params={
            'fields': 'all',
            'key': '5e35c1f55f5d7f733c060747d4496913',
            'token': 'f056846f16d58379920261708c472c9d2d2e3fe3fb6f418aa34727a9ebdd3f0b',
            'lists': 'all',
            'list_fields': 'all'
        })

    def applySessions(self, url, name, date, sender):
        return requests.post(url, params={
            'key': '5e35c1f55f5d7f733c060747d4496913',
            'token': 'f056846f16d58379920261708c472c9d2d2e3fe3fb6f418aa34727a9ebdd3f0b',
            'idList': '5cd3d9e97936a83264b363b2',
            'name': name,
            'due': date,
            'desc': sender
        })
