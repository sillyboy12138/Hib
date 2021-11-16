from time import sleep
from Test_day01 import Key
import threading
def JD():
    key=Key('chore')
    key.open('https://www.jd.com/')
    key.input_('xpath','//*[@id="key"]','娃哈哈')
    key.click('xpath','//*[@id="search"]/div/div[2]/button/i')
    key.click('xpath','//*[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img')
    key.switch(1)
    key.click('xpath','//*[@id="InitCartUrl"]')

def SN():
    key = Key('chorme')
    key.open('https://www.suning.com/')
    key.input_('xpath', '//*[@id="searchKeywords"]', '娃哈哈')
    key.click('xpath', '//*[@id="searchSubmit"]')
    key.click('xpath', '//*[@id="ssdsn_search_pro_baoguang-1-0-1_1_01:0070181626_10789076919"]/img')
    key.switch(1)
    key.click('xpath','//*[@id="addCart"]')

def BZ():
    key = Key('edge')
    key.open('https://www.bilibili.com/')
    key.input_('xpath', '//*[@id="nav_searchform"]/input', '武松')
    key.click('xpath', '//*[@id="nav_searchform"]/div/button')
    key.switch(1)
    key.click('xpath','//*[@id="navigator"]/div/div[1]/div[3]/ul/li[2]/a')
    key.locator('xpath', '//*[@id="nav_searchform"]/input').clear()
    sleep(3)
    key.click("xpath","//li[@class='video-item matrix']/a")
    key.switch(2)

if __name__ == '__main__':
    # JD()
    # SN()
    BZ()