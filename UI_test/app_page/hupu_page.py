from common.app import App
from selenium.webdriver.common.by import By
import time
from common.share import Asser
class Hupu_page():
    sousuokuang=(By.ID,"com.hupu.games:id/tv_banner2")
    shurukaung=(By.ID,"com.hupu.games:id/search_input")
    sousuoanniu=(By.ID,"com.hupu.games:id/search_btn_cancel")
    def __init__(self):
        self.a=Asser()
        self.app=App("hupu")
    def appsousuo(self):
        time.sleep(8)
        self.app.clic(*self.sousuokuang)
        time.sleep(3)
        self.app.send_key("NBA",self.shurukaung)
        # time.sleep(3)
        self.app.clic(*self.sousuoanniu)
        time.sleep(3)
        self.a.assert_activity(self.app.driver,"testantivity")
        self.app.quit()

