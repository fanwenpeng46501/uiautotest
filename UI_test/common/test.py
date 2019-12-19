from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
allpath="D:/python_project/UI_test/"
from selenium.webdriver.common.by import By
from common.web import Web
class Test_comm:
    def __init__(self):
        pass
        # self.dirver=webdriver.Chrome()
        # self.dirver.maximize_window()
        # self.dirver.get("http://www.baidu.com")
        # now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        # driver.get_screenshot_as_file(allpath+"/img"+now+".png")
    def element(self ,*ele):
        return self.dirver.find_element(*ele)
    def sendkey(self,v,*ele):
        self.element(*ele).send_keys(v)
    def cli(self,*ele):
        self.element(*ele).click()
# e1=(By.ID,"kw")
# e2=(By.ID,"su")
# t=Test_comm()
# # t.sendkey("test",*e1)
# # t.cli(*e2)
# t.two("test",*e1,*e2)
class A(unittest.TestCase):
    # def __init__(self):
    #     pass
        # self.i=i
    def ass(self,i):
        try:
            self.assertEqual(6,i,"NO")
            print("断言通过")
        except AssertionError:
            print("断言不通过")
    def test(self):
        self.ass(7)



if __name__=="__main__":
    dirver = webdriver.Chrome()
    dirver.maximize_window()
    dirver.get("http://www.baidu.com")
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    dirver.get_screenshot_as_file(allpath + "/img/" + now + ".png")
    #dirver.save_screenshot(allpath + "/img/" + now + ".png")

    # w=Web("chrome")
    # w.open("http://www.baidu.com")
    # w.element_wait("kw")

