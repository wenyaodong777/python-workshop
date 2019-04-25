#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    import cPickle as pickle;
except:
    import pickle;

    d = dict(url='index.html', title='首页', content='欢迎你')

    print pickle.dumps(d);
