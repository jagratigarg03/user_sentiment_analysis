# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 02:04:18 2023

@author: Jagrati Garg
"""
city=input("enter the city")
city_api="http://api.openweathermap.org/geo/1.0/direct?q="+city+"&limit=1&appid=9672d98b25abe65d9d1438d5dcbacc54"
import requests
response=requests.get(city_api)
response
response.json()[0]
latitude=str(response.json()[0]["lat"])
longitude=str(response.json()[0]["lon"])
air_api="http://api.openweathermap.org/data/2.5/air_pollution?lat="+latitude+"&lon="+longitude+"&appid=9672d98b25abe65d9d1438d5dcbacc54"
requests.get(air_api)


