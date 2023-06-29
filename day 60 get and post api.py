# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 23:40:03 2023

@author: Jagrati Garg
"""

currencyapi="https://api.freecurrencyapi.com/v1/latest?=USD_INR&apikey=JORYUIjeQUN7oLAV971tabVbCIApv6oQ1kthYpI1"
import requests
response=requests.get(currencyapi)
response
response.json()['data']['INR']


#post request
api="http://httpbin.org/post"
import requests
import json
data={
 'first':'jagrati',
 'interest':'machine learning'
 }

header={
      "content_type":"application/json",
      "content_length":len(data),
      "data":json.dumps(data)
        }

responsed=requests.post(api,data,header)
responsed
responsed.json()['form']
