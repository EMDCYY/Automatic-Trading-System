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
		wdyx = wdyx.iloc[:,0:6]
		num_time = date_to_num(wdyx.iloc[:,0])
		wdyx.iloc[:,0] = num_time

		# ochl: change the postino of c and h
		var = wdyx.iloc[:,2]
		wdyx.iloc[:,2] = wdyx.iloc[:,3]
		wdyx.iloc[:,3] = var
		wdyx.columns.values[2] = "CLOSE"
		wdyx.columns.values[3] = "HIGH"

		symbol = c2s(code)
		codeS = [symbol]*len(wdyx)
		wdyx['CODE'] = pd.Series(codeS, index=wdyx.index)
		mat_wdyx = np.array(wdyx)

		fig, ax = plt.subplots(figsize=(15,5))
		fig.subplots_adjust(bottom=0.5)
		mpf.candlestick_ochl(ax, mat_wdyx, width=0.6, colorup='r', colordown='g', alpha=1.0)
		plt.grid(True)
		plt.xticks(rotation=30)
		plt.title(code)
		plt.xlabel('Date')
		plt.ylabel('Price')
		ax.xaxis_date ()


		fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(15,8))
		mpf.candlestick_ochl(ax1, mat_wdyx, width=1.0, colorup = 'g', colordown = 'r')
		ax1.set_title('wandayuanxian')
		ax1.set_ylabel('Price')
		ax1.grid(True)
		ax1.xaxis_date()
		plt.bar(mat_wdyx[:,0]-0.25, mat_wdyx[:,5], width= 0.5)
		ax2.set_ylabel('Volume')
		ax2.grid(True)
		
	except Exception as e:
		 print(e)
	else:
		plt.show()




if __name__=='__main__':
	plotK('鸿博股份(002229)')