# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 14:20:46 2023

@author: Jagrati Garg
"""

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url="http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"
browser=webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)
sleep(2)
school_code=browser.find_element_by_name('treg')
school_code.send_keys(2000)
get_school_results=browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_results.click()

html_page=browser.page_source
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_page)
browser.quit()



