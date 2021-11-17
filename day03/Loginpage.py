from selenium import webdriver
from time import sleep

def browser(type_):
    try:
        driver=getattr(webdriver,type_)()
    except Exception as e:
        print(e)
        driver=webdriver.Chrome()
    return driver

class Loginpage:
    def __init__(self,type_):
        self.driver=browser(type_)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def open(self,url):
        self.driver.get(url)

    def locator(self,name,value):
        return self.driver.find_element(name,value)

    def input_(self,name,value,key):
        self.locator(name,value).send_keys(key)

    def click(self,name,value):
        self.locator(name,value).click()

    def getLoginSuccessResult(self):
        return self.driver.title

    def getLoginErrorResult(self,name,value):
        return self.driver.find_element(name,value).text

    def quit(self):
        self.driver.quit()