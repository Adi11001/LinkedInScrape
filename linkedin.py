'''
In this Project I have used python's selenium library to do web crawling and scrap data form linkedin pages of different companies.
The steps followed are:
1. Use selenium to login to linkedin. The emailid and password will be entered using selenium. You need to enter OTP while using it for first time
2. Once the signin is successful load the company page from which you want to scrape data
3. Locate the tag from which you want to scrape date
4. Get the text of the tag and print the data
'''

import pandas as pd
import matplotlib.pyplot as plt
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

page_url='https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

##########LinkedIn Login Details##########
username_txt='waniaditya11001@gmail.com'
password_txt='11001@ditya11001'
signin_btn_class="btn__primary--large"
##########################################

##########Scrapping class and id##########
numEmpXpath='/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[3]'
email_id = 'username'
password_id = 'password'
##########################################

#Launch the webpage in chrome window
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url=page_url)

#Wait for 3 seconds
time.sleep(3)

#Find the input box to enter emailid
email_box = driver.find_element(By.ID,email_id)
#Enter Email id
email_box.send_keys(username_txt)
time.sleep(2)

#Find the input box to enter password
password_box = driver.find_element(By.ID,password_id)
#Enter Password
password_box.send_keys(password_txt)
time.sleep(2)

#Find & press the login Button
signinBtn = driver.find_element(By.CLASS_NAME,signin_btn_class)
signinBtn.click()

#Wait for the page to load or time to enter OTP for 1st login
time.sleep(30)

#URL of company page from where you want to scrape data
company_url='https://www.linkedin.com/company/evianwater/about/'

#Open the url
driver.get(url=company_url)
time.sleep(3)

#Print the number of employees
print(driver.find_element(By.XPATH,numEmpXpath).text)

