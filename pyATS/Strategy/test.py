from matplotlib.pylab import date2num
import datetime
import matplotlib as mpl
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_time

def test():
	wdyx = ts.get_k_data('002739','2017-01-01')
