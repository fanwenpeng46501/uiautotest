from common.web import *
from selenium.webdriver.common.by import By
from common.share import log
from common.share import Asser
class Baidu_page():
    ele_kaung=(By.ID,"kw")
    ele_anniu=(By.ID,"su")
    def __init__(self):
        self.web=Web('chrome')
    def sousuo(self):
        log().info("打开地址")
        self.web.open("http://www.baidu.com")
        log().info("输入内容")
        self.web.send_key("NBA",*self.ele_kaung)
        log().info("点击搜索")
        self.web.clic(*self.ele_anniu)
        a=Asser()
        a.assert_title(self.web.driver,"NBA_百度搜索1")





