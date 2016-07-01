# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 28.

@author: jacegem@gmail.com
'''
import urllib2
import urllib
import json
from google.appengine.api import urlfetch

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


sido_list = ['서울', '경기', '부산', '대구', '인천', '대전', '울산', '강원', '충북', '충남', '광주', '전북', '전남', '경북', '경남', '제주', '세종']
sido_dic = {'충북':'충청북도', '충남':'충청남도', '전북':'전라북도', '전남':'전라남도', '경북':'경상북도', '경남':'경상남도', '세종':'세종특별자치시' }


def get_gugun_list(sido):
    sido = sido_dic.get(sido, sido)
    param = {'SIDO':sido}
    encoded = urllib.urlencode(param)
    search_gugun_url = 'http://nlotto.co.kr/lotto645Stat.do?method=searchGUGUN&'
    url = search_gugun_url + encoded
    html = urlfetch.fetch( url, headers=hdr ).content.decode('euc-kr', 'ignore')   
#     data = json.loads(html)
    dataenc = [d.encode('utf-8') for d in json.loads(html)]
#     print '--' * 20
#     print data
    return dataenc

def get_sido_store_list(sido, gugun_list):
    sido_total_list = []
    
    for gugun in gugun_list:        
        page = 1
        lastPage = 999
    
        ## 마지막 페이지를 읽어서 계속 요청해야 함.
        while (page <= lastPage):
            param = {'nowPage':str(page), 'sltSIDO':sido, 'sltGUGUN': gugun}
            encoded = urllib.urlencode(param) 
#             url = "http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&nowPage=" + str(page) + "&sltSIDO=" + sido + "&sltGUGUN=" + gugun
            url  = "http://nlotto.co.kr/game.do?method=sellerInfo645Result&searchType=1&" + encoded
            print url, "요청함", sido, gugun
            print "curpage:", page, "\tlastpage:", lastPage
#             request = urllib2.Request(url, headers=hdr)            
#             response = urllib2.urlopen(request)
#             html = response.read().decode('euc-kr', "ignore")
            html = urlfetch.fetch( url, headers=hdr ).content.decode('euc-kr', 'ignore')   
            data = json.loads(html)
            lastPage = data["pageEnd"]
            store_list = data["arr"]

            print "결과 데이터 수:", len(store_list)
            page += 1            
            sido_total_list.extend(store_list)
            print sido, " 지역 결과 데이터 수:", len(sido_total_list)
            
        
    return sido_total_list
    
    
    

def get_store_list():
    total_list = []
    for sido in sido_list:
        gugun_list = get_gugun_list(sido)        
        sido_store_list = get_sido_store_list(sido, gugun_list)
        total_list.extend(sido_store_list)

    
#     response = urllib2.urlopen(store_home_url) 
#     print response.info()
#     html = response.read()
#     print html
#     response.close()  # best practice to close the file
#     soup = BeautifulSoup(html, 'html.parser')
#     scripts = soup.find_all("script")
#     for script in scripts:
#         s = script.string
#         if isinstance(s, unicode):
#             s = s.encode('utf-8')
#         print s
#     pass
#     main_menu = soup.find(id="mainMenu")
#     lis = main_menu.find_all('li')
#     result = []
#     for i in lis:
#         result.append(i)
#     values = ','.join(str(v) for v in result)
#     return values
    
    

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
