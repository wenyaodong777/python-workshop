#!/usr/bin/python
# -*- coding: UTF-8 -*-
import aiml
from translate import Translator
import os

os.chdir('./src/alice')
alice = aiml.Kernel();
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

print(alice.respond('hello'))

# 按组合键 CTRL-C 停止循环
while True:
    translator = Translator(to_lang='en', from_lang='zh')
    backtranslator = Translator(to_lang='zh',from_lang='en')
    original = raw_input(u"请输入信息 >> ")
    message = translator.translate(original)
    print message
    response = alice.respond(message)
    print backtranslator.translate(response)