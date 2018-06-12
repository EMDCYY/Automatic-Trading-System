# coding: UTF-8
import sys
import os.path
import urllib.request
import urllib.error
import re



codeList_Url = r'http://quote.eastmoney.com/stocklist.html'

def urlTolist(url):
    try:
        codeList = []
        res = urllib.request.urlopen(url)
        html = res.read().decode('gbk')
        s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S\d\d\d\d\d\d.html">(.*?)</a></li>'
        pat = re.compile(s)
        codeList = pat.findall(html)
        
    except urllib.error.URLError as e:
        print('readCode.py-> %s' %e)

    else:
        return codeList


def saveList(codeList):
    try:
        myPath = os.path.abspath(os.path.dirname(__file__))
        openPath = os.path.join(myPath, "../../Data/AllCodeList/AllCodeList.txt")
        listTxt = open(openPath,"w+")
        for item in codeList:
            listTxt.write(item + '\n')
    
    except IOError as e:
        print('readCode.py-> %s' %e)
    
    else:
        listTxt.close()

def countCode(codeList):
    try:
        sh = 0;
        sz = 0;
        cy = 0;
        for item in codeList:
            if item[-7]=='6' :
                sh += 1
            elif item[-7]=='0':
                sz += 1
            elif item[-7]=='3' :
                cy += 1
            else:
                pass
            cnt = sh + sz + cy

    except Exception as e:
        print('readCode.py-> %s' %e)

    else:
        print('All code: {}, SH: {}, SZ: {}, CY: {}'.format(cnt, sh, sz, cy))

def checkCode(codeList):
    try:
        myPath = os.path.abspath(os.path.dirname(__file__))
        openPath = os.path.join(myPath, "../../stkCode.txt") 
        codeTxt = open(openPath,"r")
        code = codeTxt.read().split('\n')
 
    except IOError as e:
        print('readCode.py-> %s' %e)
    
    else:
        for item in code:
            if item not in codeList:
                print('{} is a wrong code'.format(item))
                sys.exit()
            else:
                pass
        return code


if __name__ == "__main__":
    allCodelist = urlTolist(codeList_Url)
    saveList(allCodelist)
    countCode(allCodelist)
    checkCode(allCodelist)

else:
    allCodelist = urlTolist(codeList_Url)
    saveList(allCodelist)
    countCode(allCodelist)
    return checkCode(allCodelist)

