# coding: UTF-8
import os
import re
import copy
import time
import datetime
import urllib.request
from splitCode import code2PreSymbol as c2ps
from stkHtml import code2Html as c2h
import requests

class minuteK:

	def __init__(self):
		self.__k = []
		self.__after_date = '2017-01-01'
		self.__timedelta = 4

	def getData(self, code):
		symbol = c2ps(code)
		url = 'http://hq.sinajs.cn/?format=text&list=' + symbol
		html = c2h().fastHtml(url)
		return html

if __name__ == "__main__":
    print(minuteK().getData('贵州茅台(600519)')[-3])
    	
          
