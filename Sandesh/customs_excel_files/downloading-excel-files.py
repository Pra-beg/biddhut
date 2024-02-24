#importing necessary libraries

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

#setting up service and driver
s=Service("D:/driver/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)

#initiating automation
driver.get("https://www.customs.gov.np/page/fts-fy-207879")
time.sleep(5)
# xp="/html/body/div[4]/div/div/div/div/div[2]/ul/li[3]/a"
# input= driver.find_element("xpath",xp)
# input.click()
# time.sleep(5)
for i in range(2,13):
    xp=f"/html/body/div[4]/div/div/div/div/div[2]/ul/li[{i}]/a"
    input= driver.find_element("xpath",xp)
    input.click()
    time.sleep(5)
    

