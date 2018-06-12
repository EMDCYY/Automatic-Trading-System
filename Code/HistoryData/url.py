 # -*- coding: utf-8 -*-

def getURL(code):
    if code[0:3] == '600' or code[0:3] == '601' or code[0:3] == '603':
        URL = 'http://hq.sinajs.cn/list=sh' + code
        return URL
    elif code[0:3] == '000' or code[0:3] == '002' or code[0:3] == '300':
        URL = 'http://hq.sinajs.cn/list=sz' + code
        return URL
    else:
        return 'No Code'
