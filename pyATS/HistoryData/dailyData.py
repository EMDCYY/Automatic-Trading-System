# coding: UTF-8
import os
import re
import copy
import time
import datetime
import urllib.request
from splitCode import code2Symbol as c2s
from stkHtml import code2Html as c2h
from minuteData import minuteK as mk

# a class representing a stock's daily K line
class dayK:

    def __init__(self):
        self.__k = []
        self.__after_date = '2016-01-01'
        self.__timedelta = 2


    def upData(self, code, after_date=None):
        try:
            if after_date == None:
                after_date = self.__after_date
            myPath = os.path.abspath(os.path.dirname(__file__))
            filePath = os.path.join(myPath, "../../Data/",code)
            if not os.path.exists(filePath):
                os.makedirs(filePath)
            dataPath='%s/%s.csv' % (filePath,code)
            print('1')

            if os.path.exists(dataPath):
                # if cached, load it locally
                self.__k = self.load(code)
                if len(self.__k)==0:
                    self.__k = self.fetch(code, self.__after_date)
                    self.__store(self.__k, dataPath)
                    return
                # get the last date in the cache date
                max_date = datetime.datetime.strptime(self.__k[-1][0],'%Y-%m-%d')
                rec_date = datetime.datetime.strptime(mk().getData(code)[-3],'%Y-%m-%d')
                print(rec_date)
                now = datetime.datetime.now()
                today3pm = now.replace(hour=15, minute=0, second=0, microsecond=0)
                print(today3pm)
                # if the date is more than 5 days old
                if now > today3pm:
                    if rec_date - max_date > datetime.timedelta(days=1):
                        # download the new data after the last date
                        fetch_k = self.__fetch(code, self.__k[-1][0])
                        self.__k += fetch_k
                        # append the download one to cache
                        self.__store(fetch_k,datapPath)
                    else:
                        pass

                else:
                    if rec_date - max_date > datetime.timedelta(days=2):
                        fetch_k = self.__fetch(code, self.__k[-1][0])
                        self.__k += fetch_k
                        # append the download one to cache
                        self.__store(fetch_k,datapPath)
                    else:
                        pass
            else:
                # if not cached, download all the history date
                print('2')
                self.__k = self.fetch(code, after_date)
                self.__store(self.__k, dataPath)
        except Exception as e:
            print(e)
        else:
            pass


    # load local cache file
    #   path: the file path
    #   return: the daily K line date in file, ascending ordered by date
    def load(self,code):
        try:
            myPath = os.path.abspath(os.path.dirname(__file__))
            filePath = os.path.join(myPath, "../../Data/",code)
            if not os.path.exists(filePath):
                print('No such file')
                sys.exit()
            dataPath='%s/%s.csv' % (filePath,code)
            fd=open(dataPath,'r')
            lines=fd.readlines()
            fd.close()
            k=[]
            for line in lines:
                items=line.split(',')
                date=items[0]
                op=float(items[1])
                hp=float(items[2])
                lp=float(items[3])
                cp=float(items[4])
                vl=float(items[5])
                am=float(items[6])
                k.append((date,op,hp,lp,cp,vl,am))
            k.sort(key=lambda x:x[0])
        except Exception as e:
            print(e)
        else:
            return k

    # store or append K line date to file
    def __store(self,k,path):
        fd=open(path,'a')
        for d in k:
            fd.write('%s,%s,%s,%s,%s,%s,%s\n' % d)
        fd.close()

    # download the histroy daily K line data after a given date
    #   after_date: the given date, all the returned data is after this date
    #   return: the daily K line data after the date, ascending ordered by date
    def fetch(self, code, after_date=None):
        try:
            if after_date == None:
                after_date = self.__after_date

            now = datetime.datetime.now()
            yesterday = now - datetime.timedelta(days=1)
            year = yesterday.year
            season=(yesterday.month+2)//3
            day_k=[]
            empty_time=0
            while True:
                time.sleep(0.2)
                k=self.fetch_season(code, year, season)
                season-=1
                if season==0:
                    year-=1
                    season=4
                if len(k)==0:
                    empty_time+=1
                    if empty_time>=5:
                        break
                    continue
                else:
                    empty_time=0
                day_k += k
                early_date = day_k[-1][0]
                if early_date <= after_date:
                    break
            k=[d for d in day_k if d[0]>after_date]
            k.sort(key=lambda x:x[0])
        except Exception as e:
            print(e)
        else:
            return k

    # download the date of a given season
    #   year: year
    #   season: season, 1~4
    #   return: the daily K line in this season, desc ascending ordered by date
    def fetch_season(self, code, year, season):
        try:
            print('{} - Year {} - Season {} send request'.format(code, year, season))
            symbol = c2s(code)
            url=(
                'http://vip.stock.finance.sina.com.cn/corp/go.php/'
                'vMS_FuQuanMarketHistory/stockid/%s.phtml?'
                'year=%s&jidu=%s'
                % (symbol,year,season)
                )

            html = c2h().getHtml(url)

            start = html.find('<table id="FundHoldSharesTable">')
            if start<0:
                raise IOError('wrong IO')
            end = html.find('</table>',start)
            if end<0:
                raise IOError('wrong IO')
            html = html[start:end]
            '''
                把所有的html标签全部消除掉，按空格分割，即可得到table中所有实际内容。
                最简单的办法就是使用正则表达式来匹配html标签，正则表达式很简单： <[^>]+>
                就是以"<"开头，以">"结尾，中间是一堆非">"字符。其实这种方法还是有缺陷的，比如在遇到这样的标签时会出错：
                <input text="<click me>">
            '''
            regex = re.compile('<[^>]+>')
            cells = re.sub(regex,'',html).split()
            k=[]
            for i in range(9,len(cells),8):
                date=cells[i]
                op=float(cells[i+1])
                hp=float(cells[i+2])
                cp=float(cells[i+3])
                lp=float(cells[i+4])
                vl=float(cells[i+5])
                am=float(cells[i+6])
                k.append((date,op,hp,lp,cp,vl,am))
            k.sort(key=lambda x:x[0],reverse=True)
        except Exception as e:
            print(e)
        else:
            return k

    # get the daily K line date
    #   return: the daily K line date
    #       it's a list, 
    #       each item is a tuple (date,open price,high price,low price,close price),
    #       the list is sort by date in ascending order
    def day_k(self):
        return copy.deepcopy(self.__k)

if __name__=='__main__':
    print(dayK().upData('贵州茅台(600519)','2016-01-01'))
