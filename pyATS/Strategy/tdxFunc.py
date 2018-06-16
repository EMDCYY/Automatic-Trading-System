# coding: UTF-8
import os
import pandas as pd
import numpy as np
import functools

def LLV(series, window):
	try:
		result = series.rolling(window).min()
	except ValueError as e:
		print(e)
	else:
		return result

def HHV(series, window):
	try:
		result = series.rolling(window).max()
	except ValueError as e:
		print(e)
	else:
		return result

def SMA(series, n, m):
	try:
		result = series.copy().fillna(0)
		for i in range(1, len(series)):
			result.loc[i] = ((n - m) * result.loc[i - 1] + m * result.loc[i]) / n   
	except ValueError as e:
		print(e)
	else:
		return result

def EMA(series, n):
		return SMA(series, n+1, 2)


if __name__ == "__main__":
	# k = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]], index=list('12345'), columns=list('ABC'))
	# k = pd.DataFrame([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
	k = pd.DataFrame([1,2,3,4,5,6])
	print(SMA(k,3,1))

