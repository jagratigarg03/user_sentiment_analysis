# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 05:23:02 2023

@author: Jagrati Garg
"""


wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
import requests
from bs4 import BeautifulSoup
data=requests.get(wiki).text
data
soup=BeautifulSoup(data,"lxml")
soup
right_table=soup.find('table', class_= 'wikitable')
right_table

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    
    #if it is first row, th(count) = 7, td(count) = 0
    #for rest of rows, th(count) = 1, td(count) = 6
    
    if len(cells) == 6:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
right_table        
import pandas as pd
df=pd.DataFrame()
df['State_UT'] = A
df['Admin_Cap'] = B
df['Legis_Cap'] = C
df['Judi_Cap'] = D
df['Year'] = E
df['Formar_Cap'] = F
df.to_csv("states.csv",index=False)
df1=pd.DataFrame(zip(A,B,C,D,E,F),columns=('A','B','C','D','E','F'))        
df1


import sqlite3 as sql
import pandas as pd
conn=sql.Connection("states.db")
conn
df.to_sql("statetable", conn)

rconn=sql.Connection("states.db")
pd.read_sql("select * from statetable",rconn)

fconn=sql.Connection("states.db")
fconn
pd.read_sql("select * from statetable where year==1956",fconn)

cursor=fconn.cursor()
cursor.execute("select * from statetable")

for records in cursor:
    print(records)

cursor.execute("select * from statetable where year==1956")
for records in cursor:
    print(records)

