# -*- coding: utf-8 -*-

# 0：”大秦铁路”，股票名字；
# 1：”27.55″，今日开盘价；
# 2：”27.25″，昨日收盘价；
# 3：”26.91″，当前价格；
# 4：”27.55″，今日最高价；
# 5：”26.20″，今日最低价；
# 6：”26.91″，竞买价，即“买一”报价；
# 7：”26.92″，竞卖价，即“卖一”报价；
# 8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
# 9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
# 10：”4695″，“买一”申请4695股，即47手；
# 11：”26.91″，“买一”报价；
# 12：”57590″，“买二”
# 13：”26.90″，“买二”
# 14：”14700″，“买三”
# 15：”26.89″，“买三”
# 16：”14300″，“买四”
# 17：”26.88″，“买四”
# 18：”15100″，“买五”
# 19：”26.87″，“买五”
# 20：”3100″，“卖一”申报3100股，即31手；
# 21：”26.92″，“卖一”报价
# (22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
# 30：”2008-01-11″，日期；
# 31：”15:05:32″，时间；

import time

class str2data():
    def __init__(self, stringList):
        self.stringList = stringList
        self.name
        self.open
        self.closeYesterday
        self.close
        self.highest
        self.lowest
        self.buy1st
        self.sell1st
        self.volume
        self.amount
        self.buy1stVol
        self.buy2ndVol
        self.buy2nd
        self.buy3rdVol
        self.buy3rd
        self.buy4thVol
        self.buy4th
        self.buy5thVol
        self.buy5th
        self.sell1stVol
        self.sell2ndVol
        self.sell2nd
        self.sell3rdVol
        self.sell3rd
        self.sell4thVol
        self.sell4th
        self.sell5thVol
        self.sell5th
        self.date
        self.time

    def name(self):
        self.name = self.stringList[0]
        return self.name

    def open(self):
        self.open = float(self.stringList[1])
        return self.open

    def closeYesterday(self):
        self.closeYesterday = float(self.stringList[2])
        return self.closeYesterday

    def close(self):
        self.close = float(self.stringList[3])
        return self.close

    def highest(self):
        self.open = float(self.stringList[4])
        return self.open

    def lowest(self):
        self.lowest = float(self.stringList[5])
        return self.lowest

    def buy1st(self):
        self.buy1st = float(self.stringList[6])
        return self.buy1st

    def sell1st(self):
        self.open = float(self.stringList[7])
        return self.open

    def volume(self):
        self.volume = float(self.stringList[8])
        return self.volume

    def amount(self):
        self.amount = self.stringList[9]
        return self.amount

    def buy1stVol(self):
        self.buy1stVol = float(self.stringList[11])
        return self.buy1stVol

    def buy2ndVol(self):
        self.buy2ndVol = float(self.stringList[12])
        return self.buy2ndVol

    def buy2nd(self):
        self.buy2nd = float(self.stringList[13])
        return self.buy2nd

    def buy3rdVol(self):
        self.buy3rdVol = float(self.stringList[14])
        return self.buy3rdVol

    def buy3rd(self):
        self.buy3rd = float(self.stringList[15])
        return self.buy3rd

    def buy4thVol(self):
        self.buy4thVol = float(self.stringList[16])
        return self.buy4thVol

    def buy4th(self):
        self.buy4th = float(self.stringList[17])
        return self.buy4th

    def buy5thVol(self):
        self.buy4thVol = float(self.stringList[18])
        return self.buy4thVol

    def buy5th(self):
        self.buy4th = float(self.stringList[19])
        return self.buy4th

    def sell1stVol(self):
        self.sell1stVol = float(self.stringList[21])
        return self.sell1stVol

    def sell2ndVol(self):
        self.sell2ndVol = float(self.stringList[22])
        return self.sell2ndVol

    def sell2nd(self):
        self.sell2nd = float(self.stringList[23])
        return self.sell2nd

    def sell3rdVol(self):
        self.sell3rdVol = float(self.stringList[24])
        return self.sell3rdVol

    def sell3rd(self):
        self.sell3rd = float(self.stringList[25])
        return self.sell3rd

    def sell4thVol(self):
        self.sell4thVol = float(self.stringList[26])
        return self.sell4thVo

    def sell4th(self):
        self.sell4th = float(self.stringList[27])
        return self.sell4th

    def sell5thVol(self):
        self.sell4thVol = float(self.stringList[28])
        return self.sell4thVol

    def sell5th(self):
        self.sell4th = float(self.stringList[29])
        return self.sell4th

    def date(self):
        self.date = time.strptime(self.stringList[30], "%Y-%m-%d")
        return self.date 

    def time(self):
        self.time = time.strptime(self.stringList[31], "%H:%M:%S")
        return self.time