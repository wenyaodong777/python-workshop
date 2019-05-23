# !/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import re
from wxpy import ResponseError
from urllib import quote

sys.path.append("helper")
from restHelper import RestTemplate
from fileHelper import FileHelper


class StoryAttachment():

    def __init__(self):
        self.reg = r'UI(\d{6})'
        self.restTemplate = RestTemplate()
        self.fileHelper = FileHelper()
        self.attachmentApi = "http://tracker.paas.cmbchina.cn/tracker/attachment/queryAttachFile?referenceId={storyId}&type=story"
        # self.attachmentApi = "http://localhost:3000/tracker/attachment/queryAttachFile?referenceId=" + storyId + "&type=story"

    def monitor(self, msg):
        storyId = re.search(self.reg, msg.text).group(1)
        try:
            response = self.restTemplate.getCmbTracker(self.attachmentApi.format(storyId=storyId))
            attachments = json.loads(response.content)["list"]
        except Exception as e:
            print e.message
            msg.chat.send(u'对不起，卡号' + storyId + u'错误，请核对后再试')
        else:
            if not attachments:
                msg.chat.send(u'对不起，卡号' + storyId + u'暂无UI附件')
                return
            msg.chat.send(u'卡号' + storyId + u'UI附件即将发送，注意查收！')
            for item in attachments:
                self.send(msg.chat, item)

    def start(self):
        print 'start story ui bot'
        return

    def send(self, chat, attachment):
        try:
            raw_url = attachment["url"].encode('utf-8')
            new_url = raw_url.replace(raw_url.rsplit('/', 1)[-1], '') + quote(raw_url.rsplit('/', 1)[-1])
            path = self.fileHelper.download(new_url,
                                            self.fileHelper.generate_file_path(attachment["fileName"]))
            content = '@' + self.fileHelper.wx_file_type(path) + '@' + path
        except Exception as e:
            print e.message
            chat.send(u'附件获取出错')
            pass
        else:
            try:
                chat.send(content)
            except ResponseError as e:
                print(e.err_code, e.err_msg)
                chat.send(u'附件发送失败！！！')
                pass
            finally:
                self.fileHelper.delete(path)
