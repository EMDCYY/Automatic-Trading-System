# coding: UTF-8
import os
import pandas as pd
from loadData import ldData as ld
from tdxFunc import *


def goldIndex(code):
	try:
		kd = ld().daily(code)
		DATE = kd.loc[:,"DATE"]
		OPEN = kd.loc[:,"OPEN"]
		HIGH = kd.loc[:,"HIGH"]
		CLOSE= kd.loc[:,"CLOSE"]
		LOW	 = kd.loc[:,"LOW"]
		VOL  = kd.loc[:,"VOL"]
		AMOUNT = kd.loc[:,"AMOUNT"]
		FACTOR = kd.loc[:,"FACTOR"]

		N = 9
		M1 = 3
		RSV = (CLOSE-LLV(LOW,N))/(HHV(HIGH,N)-LLV(LOW,N))*100
		K = SMA(RSV,5,1)
		D = SMA(K,M1,1)
		J = 3*K-2*D
		VARB2 = (RSV/2+22)*1
		VOLUM = EMA(VOL,13)
		FUNDS = EMA(AMOUNT, 13)
		FILTER = FUNDS/VOLUM*FACTOR
		PURIFY = ((CLOSE-FILTER)/FILTER)*100
		# gold = ((purify<0)) AND ZXNH
		# buylow = 

	# # 黄金:=((提纯 < (0)) AND ZXNH),COLORRED;
	# # 低买:IF(黄金 AND RSV<VARB2-2,50,0),COLORRED,LINETHICK2;
	# # 高卖:=IF(黄金 AND RSV>VARB2,80,120),COLORGREEN,LINETHICK2;
	# # 上涨分界:25;
	# # STICKLINE(低买,0,25,2,0),COLORYELLOW;{0,25指高度};
	# a = [1,2]
	# b = a
	# b = b+[2,3]



	except Exception as e:
		print(e)
	else:
		return (K,D,J)


if __name__ == "__main__":
    print(goldIndex('鸿博股份(002229)'))
    	

