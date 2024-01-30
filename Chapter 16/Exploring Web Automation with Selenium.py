#Exploring browser automation with Selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

obj_Chrome_Options = webdriver.ChromeOptions()

obj_Chrome_Options.add_experimental_option("excludeSwitches",["enable-automation"])

obj_Service = Service(r"C:\Users\dell\chromedriver-win64\chromedriver.exe")

obj_Driver = webdriver.Chrome(options=obj_Chrome_Options,service=obj_Service)

obj_Driver.get("https://www.wikipedia.org/")

#Get the search textbox element 
text = obj_Driver.find_element(By.ID,"searchInput")

#Type text into the textbox element
text.send_keys("Machine Learning")

#Press the enter key
text.send_keys(Keys.ENTER)  




