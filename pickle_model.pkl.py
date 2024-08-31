# -*- coding: utf-8 -*-
"""
Created on Thu May  4 00:24:00 2023

@author: Jagrati Garg
"""

import pandas as pd
df=pd.read_csv('Balanced_reviews.csv')
df.isnull().any(axis=0)
df['reviewText'][0]

#handling missing value
df.dropna(inplace=True)
df.shape
df['overall'].value_counts()

#removing the data whose overall value is 3 because we want only (negative and positive value)
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

from sklearn.feature_extraction.text import TfidfVectorizer 
vect=TfidfVectorizer(min_df=5).fit(feature_train)
len(vect.get_feature_names())
vect.get_feature_names()[10000:10010]
vectorize_feature=vect.transform(feature_train)

#create a classifier
# I use logistic regression

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(vectorize_feature,label_train)
pred=model.predict(vect.transform(feature_test))

#we check accuracy
from sklearn.metrics import roc_auc_score
roc_auc_score(label_test,pred)

import pickle
file=open('pickle_model.pkl','wb')
pickle.dump(model, file)

pickle.dump(vect.vocabulary_, open('features.pkl', 'wb'))

file=open('pickle_model.pkl','rb')
recreated_model=pickle.load(file)
recreated_model

def check_review(textdata):
    file=open('pickle_model.pkl','rb')
    vect.transform(textdata)
    recreated_model=pickle.load(file)
    
    