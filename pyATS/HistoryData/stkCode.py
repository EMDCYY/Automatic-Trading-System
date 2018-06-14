# coding: UTF-8
import sys
import os.path
import urllib.request
import urllib.error
import re

codeListURL = r'http://quote.eastmoney.com/stocklist.html'

class readCode:

    def __init__(self):
        self.__url = codeListURL
        self.__allCode = []
        self.__stkCode = []
   
    def __readStkCode(self):
        try:
            myPath = os.path.abspath(os.path.dirname(__file__))
            openPath = os.path.join(myPath, "../../stkCode.txt") 
            if not os.path.exists(openPath):
                print('No Stock Code')
                sys.exit()
            codeTxt = open(openPath,"r")
            self.__stkCode = codeTxt.read().split('\n')
            codeTxt.close()
        except IOError as e:
            print(e)        
        else:
            return self.__stkCode

    def __readAllCode(self):
        try:
            myPath = os.path.abspath(os.path.dirname(__file__))
            openPath = os.path.join(myPath, "../../Data/AllCodeList/AllCodeList.txt")
            if not os.path.exists(openPath):
                self.__urlTolist()
                self.__saveList()
                self.__countCode()
            codeTxt = open(openPath,"r")
            self.__allCode = codeTxt.read().split('\n')
            codeTxt.close()
        except IOError as e:
            print(e)
        
        else:
            return self.__allCode


    def __urlTolist(self, url=None):
        try:
            if url is None:
                url =self.__url
            codeList = []
            res = urllib.request.urlopen(url)
            html = res.read().decode('gbk')
            res.close()
            s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S\d\d\d\d\d\d.html">(.*?)</a></li>'
            pat = re.compile(s)
            self.__allCode = pat.findall(html)
        except urllib.error.URLError as e:
            print(e)
        else:
            return self.__allCode


    def __saveList(self, allCode=None):
        try:
            if allCode is None:
                allCode =self.__allCode
            myPath = os.path.abspath(os.path.dirname(__file__))
            openPath = os.path.join(myPath, "../../Data/AllCodeList/AllCodeList.txt")
            listTxt = open(openPath,"w+")
            for item in allCode:
                listTxt.write(item + '\n')
            listTxt.close()
        except IOError as e:
            print(e)       
        else:
            pass

    def __countCode(self, allCode=None):
        try:
            if allCode is None:
                allCode =self.__allCode
            sh = 0;
            sz = 0;
            cy = 0;
            for item in allCode:
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
            print(e)
        else:
            print('All code: {}, SH: {}, SZ: {}, CY: {}'.format(cnt, sh, sz, cy))


    def checkCode(self):
        try:
            self.__readStkCode()
            self.__readAllCode()
            for item in self.__stkCode:
                if item not in self.__allCode:
                    self.__urlTolist()
                    self.__saveList()
                    self.__countCode()
                    break
                else:
                    pass
            for item in self.__stkCode:
                if item not in self.__allCode:
                    print('{} is a wrong code'.format(item))
                    sys.exit()
                else:
                    pass           
            uniqueCode = set(self.__stkCode)

        except IOError as e:
            print(e)        
        else:
            return uniqueCode


if __name__ == "__main__":
    print(readCode().checkCode())




