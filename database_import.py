# -*- coding: utf-8 -*-
"""
Created on Sun May 13 08:40:36 2018

Use the database EXASOL and get some data into the appropriate shape

@author: Wolfgang Kapferer
"""
import pyexasol

def database_read(sql):
    
    connection = pyexasol.connect(dsn='IP:PORT', user='USER', password='PASSWD')
    statement = connection.execute(sql)
    
    result = statement.fetchall()
    statement.close()
    connection.close()
    
    transposed = list(zip(*result))
    
    data = [list(i) for i in transposed]
    
    return data