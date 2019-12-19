import unittest
from common.share import log
from app_page.hupu_page import Hupu_page
class Test_baidu(unittest.TestCase):
    def setUp(self):
        log().info("=====第一条测试用例开始======")
        self.hupu=Hupu_page()
    def test001(self):
        self.hupu.appsousuo()
        log().info("=====第一条测试用例结束======")
if __name__=="__main__":
    unittest.main()