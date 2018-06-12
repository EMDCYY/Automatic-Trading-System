 # -*- coding: utf-8 -*-
import sys
import time
import MySQLdb

from datetime import datetime 

from requestGet import requestGet
from url import getURL
from split import split
from str2data import str2data
from workSchedule import workSchedule

import win32api, win32con
from mouseCursor import click
from keyStroke import keyPress
from saveTXT import saveTXT
from saveExcel import wrExcel
from mysql import mySQL

reload(sys)                      
sys.setdefaultencoding('utf-8')

code = '002407'
myExcel = wrExcel(code, str(datetime.now().strftime("%y-%m-%d")))
myExcel.set()

cnt  = 1 # row number of excel

mysql = mySQL()
mysql.cnx()
mysql.cur()
mysql.createTable(code)

while (not workSchedule().ifEnd()):
# while True:
    
    if workSchedule().ifWork():
    # if True:
        
        if workSchedule().ifSample():
            dataStr = requestGet(getURL(code))
            dataList = split(dataStr)
            dataList[0] = code
            

            dateStr = dataList[-3]
            timeStr = dataList[-2]
            saveTXT(code, dateStr, timeStr, dataStr)
            myExcel.write(cnt, dataList)
            mysql.inertValue(code, dataList)
            mysql.commit()

            price = str2data(dataList)

            cnt  = cnt + 1
            print(cnt)

            time.sleep(1) 
            # The code began to run at XX:XX:00. But sometimes its work can be finished in 1 second. 
            # So I add a dealy time to avoid running code with multiple cycles in 1 second.
        else:
            pass
   
    else:
        pass

mysql.close()
myExcel.close()
