# -*- coding: utf-8 -*-
"""
Created on Wed May 16 19:45:18 2018

write data into the database

@author: Wolfgang Kapferer
"""

import pyexasol as E
import pandas as pd

def database_write(data):
    
    connection = E.connect(dsn='IP:PORT to database', user='user', password='passwd',schema='DATEN',compression=True)
    
    df = pd.DataFrame(data)
    connection.import_from_pandas(df, 'DATEN.DEFAULT_CREDIT_CARD_RESULT')
    stmt = connection.last_statement()
    print(f'IMPORTED {stmt.rowcount()} rows in {stmt.execution_time}s WITH compression')
    
    
    connection.close()
    
    print("done")