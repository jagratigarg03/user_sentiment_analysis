# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:00:54 2023

@author: Jagrati Garg
"""

url="https://api.freecurrencyapi.com/v1/latest?=USD_INR&compact=ultra&apikey=JORYUIjeQUN7oLAV971tabVbCIApv6oQ1kthYpI1"
import requests
response=requests.get(url)
response.json()
