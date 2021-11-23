from appium import webdriver

class Weibo:

    def open(self,url,params):
        self.driver = webdriver.Remote(url,params)
        self.driver.implicitly_wait(50)

    def locator(self,name,value):
        return self.driver.find_element(name,value)

    def input_(self,name,value,key):
        self.locator(name,value).send_keys(key)

    def click(self,name,value):
        self.locator(name,value).click()

    def title(self,name,value):
        return self.locator(name,value).text



