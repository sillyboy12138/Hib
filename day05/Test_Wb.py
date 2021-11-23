from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from Weibo import Weibo
import unittest
from unittest import TestCase
from ddt import ddt,data
@ddt
class Test_wb(TestCase):
    def setUp(self) -> None:
        self.url = r'127.0.0.1:4723/wd/hub'
        self.params = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1",
            "appPackage": "com.sina.weibo",
            "appActivity": "com.sina.weibo.VisitorMainTabActivity"
        }
        self.wb = Weibo()
        self.wb.open(self.url, self.params)
        self.wb.click(MobileBy.ACCESSIBILITY_ID, '我')
        self.wb.click("id", "com.sina.weibo:id/iv_psw")
        self.wb.click("id", "com.sina.weibo:id/et_login_view_uname")
        self.wb.input_('id', 'com.sina.weibo:id/et_login_view_uname', '18309472190')
        self.wb.input_('id', 'com.sina.weibo:id/et_login_view_psw', '980922wanglu')
        self.wb.click("id", "com.sina.weibo:id/iv_login_view_protocol")
        self.wb.click('id', 'com.sina.weibo:id/btn_login_view_psw')
        self.wb.click('id', 'com.sina.weibo:id/et_input')
        sleep(20)
        self.wb.click('xpath','/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]')
        self.wb.click("id", "com.sina.weibo:id/btn_login_view_psw")
        sleep(10)
        self.wb.click('xpath','/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]')

    def tearDown(self) -> None:
        self.wb.driver.quit()
    @data('推荐')
    def test_First(self,expect):
        self.wb.click(MobileBy.ACCESSIBILITY_ID,'首页')
        self.wb.click('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')
        self.wb.click('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup')
        self.wb.click('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.ImageView')
        self.wb.click("id","com.sina.weibo:id/detail_activity_header_left_button_text")
        self.wb.click("xpath","(//android.widget.ImageView[@content-desc=\"喜欢\"])[3]")
        self.wb.click('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView')
        result=self.wb.title('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')
        self.assertEqual(result,expect)
    @data('推荐')
    def test_Video(self,expect):
        self.wb.click(MobileBy.ACCESSIBILITY_ID,"视频")
        self.wb.click("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[1]")
        self.wb.click("xpath", "(//android.widget.ImageView[@content-desc=\"喜欢\"])[2]")
        self.wb.click("id", "com.sina.weibo:id/btn_close")
        self.wb.click("id", "com.sina.weibo:id/tv_search_keyword")
        result=self.wb.title('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.TextView')
        self.assertEqual(result,expect)
    @data('综合')
    def test_Select(self,expect):
        self.wb.click(MobileBy.ACCESSIBILITY_ID,"发现")
        self.wb.click("id", "com.sina.weibo:id/tv_search_keyword")
        self.wb.input_("id", "com.sina.weibo:id/tv_search_keyword","鬼畜视频")
        self.wb.driver.keyevent(84)
        self.wb.click("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout")
        self.wb.click("id", "com.sina.weibo:id/back")
        self.wb.click("id", "com.sina.weibo:id/btn_search_or_back")
        result=self.wb.title('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.TextView')
        self.assertEqual(result,expect)
    @data('@我的')
    def test_Message(self,expect):
        self.wb.click(MobileBy.ACCESSIBILITY_ID,"消息")
        self.wb.click("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.RelativeLayout")
        self.wb.click(MobileBy.ACCESSIBILITY_ID,"返回")
        self.wb.click("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout")
        self.wb.click(MobileBy.ACCESSIBILITY_ID,"返回")
        self.wb.click(MobileBy.ACCESSIBILITY_ID,"我")
        self.wb.click("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView[3]")
        self.wb.click("id", "com.sina.weibo:id/exitAccountContent")
        self.wb.click("xpath","/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]")
        result=self.wb.title('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView')
        self.assertEqual(result,expect)
if __name__ == '__main__':
    unittest.main()