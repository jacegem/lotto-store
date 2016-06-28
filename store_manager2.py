'''
Created on 2016. 6. 28.

@author: jacegem@gmail.com
'''
import urllib2



def get_store_list():
    response = urllib2.urlopen('http://pythonforbeginners.com/')
    print response.info()
    html = response.read()
    # do something
    response.close()  # best practice to close the file
    return ['a','c']


