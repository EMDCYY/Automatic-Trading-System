# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pylab import date2num
import mpl_finance as mpf
import datetime
from loadData import ldData as ld
from splitCode import code2Symbol as c2s
# import numpy.ndarray

def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_time


def plotK(code, date=None):
	try:
		wdyx = ld().daily(code)
		if date == None:
			date = "0000-00-00"
		# ohcl
		mat_wdyx = wdyx.iloc[:,0:6]
		num_time = date_to_num(mat_wdyx.iloc[:,0])
		mat_wdyx.iloc[:,0] = num_time
		
		# ochl: change the postino of c and h
		var = mat_wdyx.iloc[:,2]
		mat_wdyx.iloc[:,2] = mat_wdyx.iloc[:,3]
		mat_wdyx.iloc[:,3] = var
		mat_wdyx.columns.values[2] = "CLOSE"
		mat_wdyx.columns.values[3] = "HIGH"

		symbol = c2s(code)
		codeS = [symbol]*len(mat_wdyx)
		mat_wdyx['CODE'] = pd.Series(codeS, index=mat_wdyx.index)


		fig, ax = plt.subplots(figsize=(15,5))
		fig.subplots_adjust(bottom=0.5)
		mpf.candlestick_ochl(ax, mat_wdyx, width=0.6, colorup='g', colordown='r', alpha=1.0)
		# plt.grid(True)
		# plt.xticks(rotation=30)
		# plt.title(code)
		# plt.xlabel('Date')
		# plt.ylabel('Price')
		# ax.xaxis_date ()
	except Exception as e:
		 print(e)
	else:
		return mat_wdyx




if __name__=='__main__':
	print(plotK('鸿博股份(002229)'))