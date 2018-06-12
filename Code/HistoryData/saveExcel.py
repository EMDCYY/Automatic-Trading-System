 # -*- coding: utf-8 -*-
import sys
import xlsxwriter
import xlrd

from datetime import datetime

reload(sys)                      
sys.setdefaultencoding('utf-8')

from os.path import expanduser

class wrExcel():
    def __init__(self, code, date):
        self.home = expanduser("~")
        self.code = code
        self.date = date
        self.filename = code + '#' + date + '.xlsx'

        self.excel = xlsxwriter.Workbook("{}/Desktop/".format(self.home)+self.filename)
        self.sheet = []

        self.initString = ['Name', 'Open', 'CloseYesterday', 'Close', 'Highest', 'Lowest', 'Buy1st', 'Sell1st', 'Volume', 'Amount', 
        'Buy1stVol', 'Buy1st', 'Buy2ndVol', 'Buy2nd', 'Buy3rdVol', 'Buy3rd', 'Buy4thVol', 'Buy4th', 'Buy5thVol', 'Buy5th', 
        'Sell1stVol', 'Sell1st', 'Sell2ndVol', 'Sell2nd', 'Sell3rdVol', 'Sell3rd', 'Sell4thVol', 'Sell4th', 'Sell5thVol', 'Sell5th', 
        'Date', 'Time']

    
    def set(self):
        self.sheet = self.excel.add_worksheet(self.code)
        for col in range (len(self.initString)):
            self.sheet.write(0, col, "{}".format(self.initString[col]))

    def write(self, row, data):
        for col in range (len(data)):
            self.sheet.write(row, col, "{}".format(data[col]))
        # self.sheet.write(2, 2, xlwt.Formula("A3+B3"))

    def close(self):    
        self.excel.close()


    def read(self):
        wbRD = xlrd.open_workbook("{}/Desktop/".format(self.home)+self.filename)
        self.sheet = wbRD.sheets()
        # print("The number of worksheets is {0}".format(book.nsheets))
        # print("Worksheet name(s): {0}".format(book.sheet_names()))
        # sh = book.sheet_by_index(0)
        # print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
        # print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
        # for rx in range(sh.nrows):
        # print(sh.row(rx))

    def reWrite(self, row, data):
        self.read()
        wbRW = xlsxwriter.Workbook("{}/Desktop/".format(self.home)+self.filename)
        for sheet in self.sheet: # write data from old file
            newSheet = wbRW.add_worksheet(sheet.name)
            for row in range(sheet.nrows):
                for col in range(sheet.ncols):
                    newSheet.write(row, col, sheet.cell(row, col).value)
            for col in range (len(data)):
                newSheet.write(row, col, "{}".format(data[col]))

# Test:
# p = wrExcel('123','456')
# p.set()
# p.write(2,['23',234])
# p.write(3,[1,2,'a','g'])
# p.close()
# p.reWrite(3,[3,4])
# p.close()





