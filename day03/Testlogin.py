import datetime
import unittest
from unittest import TestCase
import xlrd
from ddt import ddt,data,unpack
from Loginpage import Loginpage
import openpyxl
import xlwt
from xlutils import copy

wb=openpyxl.load_workbook(r'C:\Users\呆瓜\Desktop\day03.xlsx')
sheet=wb.sheetnames
listt=[]
for name in sheet:
    for value in wb[name].values:
        if type(value[0]) is not int:
            pass
        else:
            params = {}
            params['row']=value[0]
            params['username']=value[1]
            params['password']=value[2]
            params['expect']=value[3]
            listt.append(params)
@ddt
class Testlogin(TestCase):
    def setUp(self) -> None:
        self.login=Loginpage('Chrome')
        self.login.open('http://localhost:8080/HKR/')
    def tearDown(self) -> None:
        self.login.quit()

    @data(*listt)
    @unpack
    def test_login(self,username,password,expect,row):
        self.login.input_('xpath','//*[@id="loginname"]',username)
        self.login.input_('xpath','//*[@id="password"]',password)
        self.login.click('xpath','//*[@id="submit"]')
        if self.login.getLoginSuccessResult()=='Student Login':
            result = self.login.getLoginSuccessResult()
        else:
            result=self.login.getLoginErrorResult('xpath','//*[@id="msg_uname"]')
        self.assertEqual(expect,result)
        wd=xlrd.open_workbook(r'C:\Users\呆瓜\Desktop\day03.xlsx')
        wd=copy.copy(wd)
        worksheet=wd.get_sheet(0)
        if expect==result:
            worksheet.write(row,4,'pass')
            wd.save(r'C:\Users\呆瓜\Desktop\day03.xlsx')
        else:
            worksheet.write(row,4,'false')
            wd.save(r'C:\Users\呆瓜\Desktop\day03.xlsx')

if __name__ == '__main__':
    unittest.main()

