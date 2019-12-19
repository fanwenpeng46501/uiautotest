import logging
import time
import configparser,os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest
#项目所在路径，以便进行全局路径读取
allpath="D:/python_project/UI_test/"
now=time.strftime("%Y%m%d%H%M%S", time.localtime())
#获取配置文件信息
def ini(section,option):
    con=configparser.ConfigParser()
    con.read(allpath+"config/config.ini")
    vaule=con.get(section,option)
    return vaule
#log日志配置
def log():
    # now=time.strftime("%Y%m%d%H%M%S", time.localtime())
    logPath = allpath+"/log/"+now+".log"
    FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    logging.basicConfig(level=logging.INFO,filename=logPath, format=FORMAT)
    return logging
class Common:
    def __init__(self):
        pass
    # 元素定位
    def element(self, *ele):
        return self.driver.find_element(*ele)
    # 组定位
    def elements(self, *ele):
        return self.driver.find_elements(*ele)
    # 显式等待
    def element_wait(self, ele):
        WebDriverWait(self.driver, 6, 1).until(EC.presence_of_element_located((ele)))
    # 发送内容
    def send_key(self,text,*ele):
        self.element(*ele)
        e1 = self.element(*ele)
        e1.clear()
        e1.send_keys(text)
    # 清空输入框内容
    def clear(self, *ele):
        self.element_wait(ele)
        e1 = self.element(*ele)
        e1.clear()
    # 单击
    def clic(self, *ele):
        self.element_wait(ele)
        e1 = self.element(*ele)
        e1.click()
    #后退
    def back(self):
        self.driver.back()
    #前进
    def forward(self):
        self.driver.forward()
    #截图

class Asser(unittest.TestCase):
    #截图
    def take_Shot(self,driver):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        driver.get_screenshot_as_file(allpath+"/img/"+now+".png")
    # 判断元素是否存在
    def isElementPresent(self,driver,*ele):
        try:
            element = driver.find_element(*ele)
        except NoSuchElementException as e:
            return False
        else:
            return True
    # url断言
    def assert_url(self,driver,exp_url):
        try:
            self.assertEqual(driver.current_url, exp_url, "URL断言失败")
        except AssertionError:
            log().info("URL断言失败")
            self.take_Shot(driver)
    #标题断言
    def assert_title(self,driver,exp_title):
        try:
            self.assertEqual(driver.title, exp_title,"标题断言失败")
        except AssertionError:
            log().info("标题断言失败")
            self.take_Shot(driver)
    #activity断言
    def assert_activity(self,driver,exp_activity):
        try:
            self.assertEqual(driver.current_activity, exp_activity,"activity断言失败")
        except AssertionError:
            log().info("activity断言失败")
            self.take_Shot(driver)
    #元素是否存在断言
    def assert_ifhasele(self,driver,*exp_ele):
        try:
            self.assertTrue(self.isElementPresent(driver,*exp_ele),"元素存在断言失败")
        except AssertionError:
            log().info("元素存在断言失败")
            self.take_Shot(driver)



