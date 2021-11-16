import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
def browser(type_):
    try:
        driver=getattr(webdriver,type_)()
    except Exception as e:
        print("无",type_,"浏览器，默认使用Chrome")
        driver=webdriver.Chrome()
    return driver

class Key:
    def __init__(self,type_):
        self.driver=browser(type_)
        self.driver.implicitly_wait(10)

    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def locator(self,name,value):
        return self.driver.find_element(name,value)

    def input_(self,name,value,key):
        self.locator(name,value).send_keys(key)

    def click(self,name,value):
        self.locator(name,value).click()

    def switch(self,index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def quit(self):
        self.driver.quit()


