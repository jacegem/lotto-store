# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 28.

@author: jacegem@gmail.com
'''
import urllib2
import json

# 한글입력가능?
# TODO: beautifulsoup 을 사용하자.

from bs4 import BeautifulSoup
from store import Store

hdr = {
    'accept': 'application / json',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en - US, en;q = 0.8',
    'user-agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 51.0.2704.103 Safari / 537.36',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
url = 'http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&'

store_home_url = 'http://nlotto.co.kr/game.do?method=sellerInfo645'
search_gugun_url = 'http://nlotto.co.kr/lotto645Stat.do?method=searchGUGUN'

sido_list = ['서울', '경기', '부산', '대구', '인천', '대전', '울산', '강원', '충북', '충남', '광주', '전북', '전남', '경북', '경남', '제주', '세종']


def get_gugun_list(sido):
    search_url = search_gugun_url + "&SIDO=" + sido;
    request = urllib2.Request(search_url, headers=hdr)
    response = urllib2.urlopen(request)
    html = response.read().decode('euc-kr', "ignore")
    data = json.loads(html)
    dataenc = [d.encode('utf-8') for d in json.loads(html)]
    print '--' * 20
    print data
    return data

def get_store_list():
    gugun = get_gugun_list()
    
    response = urllib2.urlopen(store_home_url) 
    print response.info()
    html = response.read()
    print html
    response.close()  # best practice to close the file
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all("script")
    for script in scripts:
        s = script.string
        if isinstance(s, unicode):
            s = s.encode('utf-8')
        print s
    pass
    main_menu = soup.find(id="mainMenu")
    lis = main_menu.find_all('li')
    result = []
    for i in lis:
        result.append(i)
    values = ','.join(str(v) for v in result)
    return values
    
    

def get_store_list2():
    url = 'http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&nowPage=1&sltSIDO=서울&sltGUGUN=강남구'
    request = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(request)
   
    html = response.read()
#     decode = html.decode('cp949', "ignore")
    decode = html.decode('euc-kr', "ignore")#.encode('utf-8')
    # json.loads 를 하면 unicode로 반환된다.
    data = json.loads(decode)
    
    for d in data['arr']:
        print d

        s = Store()      
#         k = s.make_key(d["RECORDNO"]).get()
#         print k  
        s.key = d["RTLRID"]
        s.RTLRID = d["RTLRID"]        
        s.RECORDNO = d["RECORDNO"]
#         s.save(d)
        s.put()
        
        
        
        for key in d:
#             key = str(k)             
#             val = d[k]
            if isinstance(key, unicode): 
                key = key.encode('utf-8')
                
            val = d[key]             
            if isinstance(val, unicode):
                val = val.encode('utf-8')
            
#             if isinstance(val, unicode):
#                 val = val.encode('utf-8')
                
#             if val is None:
#                 val = ""       
#             elif isinstance(val, int) or isinstance(val, float):
#                 val = val
#             else:       
#                 val = val.encode('utf-8')

            print "key:{0}\tdata:{1}".format(key, val)
        print "-" * 20;    
    text = json.dumps(decode)
    return text



def bs4_read():
    response = urllib2.urlopen('http://pythonforbeginners.com/')
    print response.info()
    html = response.read()
    response.close()  # best practice to close the file
    soup = BeautifulSoup(html, 'html.parser')
    alla = soup.find_all('a')
    result = []
    for i in alla:
        result.append(i)
    values = ','.join(str(v) for v in result)
    return values
