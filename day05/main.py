import os
import unittest
from HTMLTestRunner import HTMLTestRunner


tests=unittest.defaultTestLoader.discover(os.getcwd(),pattern='Test*.py')

runner=HTMLTestRunner.HTMLTestRunner(
    title='测试报告',
    description='微博测试',
    verbosity=1,
    stream=open(file='Wb.html',mode='w+',encoding='utf-8')
)
runner.run(tests)
