#%%
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select 
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import NoAlertPresentException 
from selenium.webdriver.common.keys import Keys 
import unittest 
from selenium.webdriver.support.select import Select 
import time 
from selenium.webdriver.support.ui  import WebDriverWait 
import os 
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile 
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv")

driver = webdriver.Firefox(firefox_profile=fp) 
driver.get("https://data.iledefrance.fr/explore/?refine.theme=D%C3%A9placements+-+transports&sort=modified")
driver.find_element_by_link_text('Export').click()
#driver.find_element_by_link_text('Jeu de données entier').click()
driver.find_element_by_xpath('//ul[1]/li[1]/div/a').click()