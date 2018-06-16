 # -*- coding: utf-8 -*-

def code2Symbol(code):
    symbol = '{}{}{}{}{}{}'.format(code[-7],code[-6],code[-5],code[-4],code[-3],code[-2])
    return symbol

def code2PreSymbol(code):
    symbol = '{}{}{}{}{}{}'.format(code[-7],code[-6],code[-5],code[-4],code[-3],code[-2])
    if symbol[0]=='6':
    	symbol = 'sh'+symbol
    elif symbol[0]=='0':
    	symbol = 'sz'+symbol
    elif symbol[0]=='3':
    	symbol = 'sz'+symbol
    else:
    	pass
    return symbol

if __name__ == "__main__":
    print(code2PreSymbol('贵州茅台(600519)'))