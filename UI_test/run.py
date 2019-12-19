import unittest,os,time
from BeautifulReport import BeautifulReport

test_dir = './testcase'

now = time.strftime("%Y%m%d%H%M%S", time.localtime())
def run_app():
    # 定义测试报告
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='apptest*.py')
    BeautifulReport(discover).report(filename='UI自动化测试报告'+now, description='测试用例', log_path='./report/')
def run_web():
    # 定义测试报告
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='webtest*.py')
    BeautifulReport(discover).report(filename='UI自动化测试报告'+now, description='测试用例', log_path='./report/')


if __name__=="__main__":
    run_web()
