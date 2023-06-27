from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)

time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) #brand start - 1
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 2 start
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 3
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 2 start
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand-4
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 2 start
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 3
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 5 start
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand-6
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 7 start
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 3
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 8 start
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand-4
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 9 start
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 3
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on next channel.
#brand - 10 start
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item/div').click() #click on next channel.
time.sleep(2)
with open("urls.txt") as f:
     for url in f:
         driver.get(url)  #replace with url in urls text file
time.sleep(5)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > yt-smartimation > yt-button-shape').click() #click on subscribe button. 
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[3]/a').click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item/div').click() #click on next channel.
#BE INFINITY.. 