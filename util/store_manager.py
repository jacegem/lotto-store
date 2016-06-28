# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 28.

@author: jacegem@gmail.com
'''
import urllib2

# 한글입력가능?
#TODO: beautifulsoup 을 사용하자.

from bs4 import BeautifulSoup


def get_store_list():
    response = urllib2.urlopen('http://pythonforbeginners.com/')
    print response.info()
    html = response.read()
    # do something 
    response.close()  # best practice to close the file
    
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    soup.find_all('a')
    return html


