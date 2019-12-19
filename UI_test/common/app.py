from appium import webdriver
from common.share import Common
from appium.webdriver.common.touch_action import TouchAction
from config.confi import ini
class App(Common):
    #初始化启动APP
    def __init__(self,appname):
        des = {}
        des["appPackage"] = ini(appname,"appPackage")
        des["appActivity"] = ini(appname,"appActivity")
        des["platformName"] = ini(appname,"platformName")
        des["deviceName"] = ini(appname,"deviceName")
        des["platformVersion"] = ini(appname,"platformVersion")
        des["udid"] = ini(appname,"udid")
        des["unicodeKeyboard"] = "True"  # 使用unicode编码方式发送字符串
        des["resetKeyboard"] = "True"  # 隐藏键盘
        des["noReset"] = "True"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=des)

    #屏幕下滑
    def swipe_Down(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)
    #屏幕上滑
    def swipe_Up(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
    #屏幕左滑
    def swipe_Left(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)
    #屏幕右滑
    def swipe_Rigth(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)
    #关闭APP
    def close(self):
        self.driver.close_app()
    #退出APP
    def quit(self):
        self.driver.quit()
    #启动APP
    def launch(self):
        self.driver.launch_app()
    #移除APP
    def remove(self,package):
        self.driver.remove_app(package)
    #安装APP
    def install(self,app_path):
        self.driver.install_app(app_path)
    #点击某个元素
    def tap(self,*ele):
        e1=self.element(*ele)
        TouchAction(self.driver).tap(e1)
    #移动至某个元素
    def moveto(self,*ele):
        e1 = self.element(*ele)
        TouchAction(self.driver).move_to(e1).release().perform()
    #按压
    def press(self,*ele):
        e1 = self.element(*ele)
        TouchAction(self.driver).press(e1).release().perform()
    #长按压
    def longpress(self,*ele):
        e1 = self.element(*ele)
        TouchAction(self.driver).long_press(e1).release().perform()
    def swich_context(self,context):
        self.driver.context(context)







