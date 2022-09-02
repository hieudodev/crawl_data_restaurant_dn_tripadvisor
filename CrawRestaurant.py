from __future__ import barry_as_FLUFL
from asyncio.windows_events import NULL
from cmath import pi
from itertools import count
from lib2to3.pgen2 import driver
from operator import truediv
from os import link
from re import search
from traceback import print_tb
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import numpy as np
import pandas as pd
import csv

def write_csv(row, file_name):
    with open(file_name, mode='a', newline='', encoding='utf-8-sig') as outfile:
        writer = csv.writer(outfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(row)

name_csv_cleaned = 'restaurant_dn_tripadvisor.csv'
write_csv(['Title','confirm','Address','phone','Price','dish','special_diet', 'rating', 'review'], name_csv_cleaned)


options = Options()
options.add_argument('--headless')
options.add_argument(
    'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"')

s = Service('D:\Code\Python\CrawlData\driver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://www.tripadvisor.com.vn/Restaurants-g298085-Da_Nang.html'
driver.get(url)
count = 0
def CrawlData():
  for i in range(1,45):
    try:
        elements = driver.find_elements(By.XPATH , f'//*[@id="component_2"]/div/div[{i}]/div/span/div[1]/div[2]/div[1]/div/span/a')
        for i in elements:
          if i != []:
            # print("i : ", i)
            # print(i.get_attribute('href'))

            driver_detail = webdriver.Chrome(executable_path=r'D:\Code\Python\CrawlData\driver\chromedriver.exe')
            driver_detail.get(i.get_attribute('href'))

            title_detail = driver_detail.find_element(By.CLASS_NAME,"HjBfq").get_attribute('textContent')
            print("title : ",title_detail)

            confirm_detail = driver_detail.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[4]/div/div/div[1]/div[1]/div/div/div").get_attribute('textContent')
            print("Xác nhận : ",confirm_detail)

            address_detail = driver_detail.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[4]/div/div/div[3]/span[1]/span/a").get_attribute('textContent')
            print("address :", address_detail)

            phonenumbe_detail = driver_detail.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[4]/div/div/div[3]/span[2]/span/span[2]/a").get_attribute('textContent')
            print("Sdt :",phonenumbe_detail)

            price_detail = driver_detail.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]").get_attribute('textContent')
            print("Price detail : ",price_detail)

            mon_an = driver_detail.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]").get_attribute('textContent')
            print("món ăn :",mon_an)

            che_do_an_db  = driver_detail.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[3]/div[2]").get_attribute('textContent')
            print("Chế độ ăn đặc biệt :",che_do_an_db)

            ratings_detail = driver_detail.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/span[1]" ).get_attribute('textContent')
            print("rating : ",ratings_detail)

            reviews_detail = driver_detail.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/a").get_attribute('textContent')
            print("reviews : ",reviews_detail)
            write_csv([title_detail,confirm_detail,address_detail,phonenumbe_detail,price_detail,mon_an,che_do_an_db,ratings_detail,reviews_detail], name_csv_cleaned)

            driver_detail.close()
    except:
        print("Dữ liệu trống")
CrawlData()




step = driver.find_element(By.XPATH , f'//*[@id="EATERY_LIST_CONTENTS"]/div[2]/div/a')
trang_tiep_theo = step.get_attribute('href')
driver.get(trang_tiep_theo)
CrawlData()

so_trang = 30
while so_trang > 0 :
     step = driver.find_element(By.XPATH , f'//*[@id="EATERY_LIST_CONTENTS"]/div[2]/div/a[2]')
     trang_tiep_theo = step.get_attribute('href')
     driver.get(trang_tiep_theo)
     CrawlData()
     so_trang -= 1

driver.close()






   
        



    
    




