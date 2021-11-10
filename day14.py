import unittest
from 工商银行面向对象 import Bank,chaxun
from Read_excel import get_data,write1_data,write2_data
import xlwt
from ddt import ddt,data,unpack
b=Bank()
aa=get_data(r'C:\Users\呆瓜\Desktop\icbc.xlsx',0)
bb=get_data(r'C:\Users\呆瓜\Desktop\icbc.xlsx',1)

@ddt
class MyTestCase(unittest.TestCase):
    @data(*aa)
    @unpack
    def test_transfer(self, Id, save_password, change_user, change_money, retu,row):
        ret=b.transfer(Id,save_password,change_user,change_money)
        self.assertEqual(ret,retu)
        write1_data(ret,retu,row)

    @data(*bb)
    @unpack
    def test_select(self, Id, save_password, retu,row):
        ret=chaxun(Id,save_password)
        self.assertEqual(ret,retu)
        write2_data(ret,retu,row)

if __name__ == '__main__':
    unittest.main()
