import os
import unittest
from HTMLTestRunner import HTMLTestRunner


tests=unittest.defaultTestLoader.discover(os.getcwd(),pattern='Test*.py')

runner=HTMLTestRunner.HTMLTestRunner(
    title='HKR测试报告',
    description='用户登陆测试',
    verbosity=1,
    stream=open(file='HKR.html',mode='w+',encoding='utf-8')
)
runner.run(tests)
