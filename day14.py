import unittest
from 工商银行面向对象 import Bank,chaxun
from Read_excel import get_data
import xlwt
from xlutils import copy
import xlrd
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
        wb = xlrd.open_workbook(r'C:\Users\呆瓜\Desktop\icbc.xlsx')
        wb = copy.copy(wb)
        worksheet = wb.get_sheet(0)
        if ret == retu:
            worksheet.write(row, 8, 'pass')
            wb.save('icbc.xlsx')
        else:
            worksheet.write(row, 8, 'false')
            wb.save('icbc.xlsx')

    @data(*bb)
    @unpack
    def test_select(self, Id, save_password, retu,row):
        ret=chaxun(Id,save_password)
        self.assertEqual(ret,retu)
        wb = xlrd.open_workbook(r'C:\Users\呆瓜\Desktop\icbc.xlsx')
        wb = copy.copy(wb)
        worksheet = wb.get_sheet(1)
        if ret == retu:
            worksheet.write(row, 6, 'pass')
            wb.save('icbc.xlsx')
        else:
            worksheet.write(row, 6, 'false')
            wb.save('icbc.xlsx')


if __name__ == '__main__':
    unittest.main()
