# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 28.

@author: jacegem@gmail.com
'''
import urllib2

# 한글입력가능?
#TODO: beautifulsoup 을 사용하자.

from bs4 import BeautifulSoup

hdr = {
    'accept': 'application / json',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en - US, en;q = 0.8',
    'user-agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 51.0.2704.103 Safari / 537.36',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
url = 'http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&'


def get_store_list():
    url = 'http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&nowPage=1&sltSIDO=서울&sltGUGUN=강남구'
    request = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(request)    
#     response = urllib2.urlopen('http://pythonforbeginners.com/')
    print response.info()
    html = response.read()
    decode = html.decode('cp949', "ignore")
    # do something 
    response.close()  # best practice to close the file

    soup = BeautifulSoup(html, 'html.parser')
    alla = soup.find_all('a')
    result = []
    for i in alla:
        result.append(i)
    values = ','.join(str(v) for v in result)
    return decode


