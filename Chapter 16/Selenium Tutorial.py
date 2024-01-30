#Open Chrome Browser Instance

from selenium import webdriver
 
# Webdriver object
objDriver = webdriver.Chrome()

#Open google.co.in window
objDriver.get("https://google.co.in")

