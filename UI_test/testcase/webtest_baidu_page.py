import unittest
from common.share import log
from web_page.baidu_page import Baidu_page
class Test_baidu(unittest.TestCase):
    def setUp(self):
        log().info("=====第一条测试用例开始======")
        self.baidu=Baidu_page()
    def test001(self):
        self.baidu.sousuo()
        log().info("=====第一条测试用例结束======")
if __name__=="__main__":
    unittest.main()