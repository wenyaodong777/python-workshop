#!/usr/bin/python
# -*- coding: UTF-8 -*-

import jenkins

class JenkinsServer():

    def jenkinsInit(self):
        jenkins_server_url = 'http://99.12.42.153:8080/'
        user_id = 'admin'
        api_token = 'f7b827c245916e7f7938ab58d80f579d'
        # 实例化jenkins对象，连接远程的jenkins master server
        return jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
