#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jenkins
from wxpy import *

import aiml
import os

bot = Bot(True)
my_friend = bot.friends().search(u'隐形的稻草人')
print(my_friend)





jenkins_server_url = 'http://99.12.42.153:8080/'

user_id = 'admin'
api_token = 'f7b827c245916e7f7938ab58d80f579d'





os.chdir('./src/alice')
alice = aiml.Kernel();
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

@bot.register()
def print_others(msg):
    txt = msg.text;
    print(msg)
    # 在项目过程中发现

    txt = txt.replace(u'吗', '')
    txt = txt.replace(u'么', '')
    txt = txt.replace('?',  '!')
    txt = txt.replace(u'？', '!')
    # print(txt)
    if msg.text == 'ci':

        # 实例化jenkins对象，连接远程的jenkins master server
        server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)

        # 构建test
        # print server.get_job_info("all-db-doc")  current_iteration
        # print server.get_info()["jobs"]

        jobs = server._get_view_jobs("current_iteration")
        # print server.get

        infos = []

        for job in jobs:
            infos.append(job["fullname"] + "(" + job["color"] + ")")

        str1 = ""

        for info in infos:
            str1 += info + "\r\n"

        return str1
    #if isinstance(msg.chat, Group) and not msg.is_at:
    #    return txt
    #else:
    #    return 'hello'
    return alice.respond(txt)

    


@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

embed()