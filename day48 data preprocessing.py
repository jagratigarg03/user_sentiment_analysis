# -*- coding: utf-8 -*-
"""
Created on Mon May  1 00:54:58 2023

@author: Jagrati Garg
"""

import pandas as pd
df=pd.read_csv('Balanced_reviews.csv')
df
df.head()
df.shape
df.columns
df.isnull().any(axis=0)
df['reviewText'][0]
df.dropna(inplace=True)
df.shape
df['overall'].value_counts()
df=df[df['overall']!=3]
df.shape
df['overall'].value_counts()
import numpy as np
df['positivity']=np.where(df['overall']>3,1,0)
df.shape
df['positivity'].value_counts()

features=df['reviewText']
label=df['positivity']
features
label
from sklearn.model_selection import train_test_split
feature_train,feature_test,label_train,label_test=train_test_split(features,label,random_state=42)

from sklearn.feature_extraction.text import CountVectorizer 
vect=CountVectorizer().fit(feature_train)
len(vect.get_feature_names())
vect.get_feature_names()[10000:10010]
vectorize_feature=vect.transform(feature_train)


