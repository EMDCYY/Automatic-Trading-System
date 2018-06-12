 # -*- coding: utf-8 -*-

import requests
# from bs4 import BeautifulSoup

def requestGet(URL):
    res = requests.get(URL)
    return res.text
