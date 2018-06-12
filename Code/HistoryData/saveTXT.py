 # -*- coding: utf-8 -*-

def saveTXT(code, date, time, string):
    text_file = open(code + '#' + date + '.txt', "a")
    text_file.write(time + ' -> ' + string + '\n')
    text_file.close()
