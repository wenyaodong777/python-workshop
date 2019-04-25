#!/usr/bin/python
# -*- coding: UTF-8 -*-

import jenkins

jenkins_server_url = 'http://99.12.42.153:8080/'

user_id = 'admin'
api_token = 'f7b827c245916e7f7938ab58d80f579d'

jobs = ('emall-api-')

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


for info in infos:

    print info