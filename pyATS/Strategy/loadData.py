# coding: UTF-8
import os
import pandas as pd

class ldData():
    
    def __init__(self):
        self.data = []


    def daily(self,code):
        try:
            dataPath="../../Data/%s/%s.csv" % (code,code)
            print(dataPath)
            data = pd.read_csv(dataPath)
        except Exception as e:
            print(e)
        else:
            return data

if __name__=='__main__':
    kd = ldData().daily('鸿博股份(002229)')
    print(kd)