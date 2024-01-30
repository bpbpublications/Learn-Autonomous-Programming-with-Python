#Chrome browser instance with options

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

obj_Chrome_Options = webdriver.ChromeOptions()

obj_Chrome_Options.add_experimental_option("excludeSwitches",["enable-automation"])

obj_Service = Service(r"C:\Users\dell\chromedriver-win64\chromedriver.exe")

obj_Driver = webdriver.Chrome(options=obj_Chrome_Options,service=obj_Service)

obj_Driver.get("https://www.google.co.in/")

