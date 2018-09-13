# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:14:07 2018

@author: shurastogi
"""

import sqlite3
import pandas as pd

connection = sqlite3.connect('C:\\Users\\shurastogi\\Desktop\\dataAdult.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE sqladb (age int,workclass TEXT,fnlwgt int,
            education TEXT,education_num int,marital_status TEXT,
            occupation TEXT,relationship TEXT,race TEXT,
            sex TEXT,capital_gain int, capital_loss  int,
            hours_per_week int, native_country TEXT,label TEXT)''' )

df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",sep=",\s",header=None,engine='python')
insert=cursor.executemany('INSERT INTO sqladb (age,workclass,fnlwgt,education,education_num,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,label) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ', df.values.tolist())
##Question 1
select_limit_10=cursor.execute('select * from sqladb limit 10')
for row in select_limit_10:
    print(row)

##Question 2
cursor.execute("select avg(hours_per_week) from sqladb where sex=:sex and workclass=:wk", {"sex":'Male',"wk":'Private'})
cursor.fetchall()
##Question 3
emp_ft="Select education, count(*) From   sqladb Group By education"
cursor.execute(emp_ft).fetchall()

occupation_ft="Select occupation, count(*) From   sqladb Group By occupation"
cursor.execute(occupation_ft).fetchall()

relationship_ft="Select relationship, count(*) From   sqladb Group By relationship"
cursor.execute(relationship_ft).fetchall()

##Question 4
master_married_private=cursor.execute("select * from sqladb where education=:edu and workclass=:wk and relationship in ('Husband','Wife')", {"edu":'Masters',"wk":'Private'})
for row in master_married_private:
    print(row)

##Question 5
sector_age_gp="Select workclass,avg(age),min(age),max(age) From  sqladb Group By workclass"
cursor.execute(sector_age_gp).fetchall()

##Question 6
age_distribution="select avg(age),native_country from sqladb group by native_country"
cursor.execute(age_distribution).fetchall()

##Question 7
add_new="SELECT (capital_gain - capital_loss) AS Net_Capita_lGain from sqladb"
cursor.execute(add_new)
cursor.fetchall()

