# -*- coding: utf-8 -*-
'''
Created on 2016. 6. 28.

@author: nw
'''

from google.appengine.ext import ndb


class Store(ndb.Model):
    '''
    classdocs 클래스 설명  
    '''
    key = ndb.StringProperty()
    RTLRID = ndb.StringProperty()    
    RECORDNO = ndb.IntegerProperty()    

        
    

    
    
    