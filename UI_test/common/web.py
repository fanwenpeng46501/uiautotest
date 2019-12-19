from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from common.share import Common

class Web(Common):
	# 初始化浏览器
	def __init__(self,brower):
		if brower =='firefox' or brower =='Firefox' or brower =='f' or brower =='F':
			deriver=webdriver.Firefox()
		elif brower =='Ie' or brower =='ie' or brower =='i' or brower=='I':
			deriver=webdriver.Ie()
		elif brower =='Chrome' or brower =='chrome' or brower =='Ch' or brower=='ch':
			deriver=webdriver.Chrome()
		elif brower =='PhantomJS' or brower =='phantomjs' or brower =='ph' or brower=='phjs':
			deriver=webdriver.PhantomJS()
		elif brower =='Edge' or brower =='edge' or brower =='Ed' or brower=='ed':
			deriver=webdriver.Edge()
		elif brower =='Opera' or brower =='opera' or brower =='op' or brower=='OP':
			deriver=webdriver.Opera()
		elif brower =='Safari' or brower =='safari' or brower =='sa' or brower=='saf':
			deriver=webdriver.Safari()
		else:
			raise NameError('只能输入firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari')
		self.driver=deriver
	# 打开网页
	def open(self,url):
		self.driver.get(url)
	# 最大化浏览器
	def make_maxwindow(self):
		self.driver.maximize_window()
	# 设置窗口
	def set_winsize(self,wide,hight):
		self.driver.set_window_size(wide,hight)
	# 右击
	def right_click(self,*ele):
		self.element_wait(*ele)
		e1=self.element(*ele)
		ActionChains(self.driver).context_click(e1).perform()
	# 移动到某个元素
	def move_element(self,*ele):
		self.element_wait(*ele)
		e1=self.element(*ele)
		ActionChains(self.driver).move_to_element(e1).perform()
	# 双击
	def double_click(self,*ele):
		self.element_wait(*ele)
		e1=self.element(*ele)
		ActionChains(self.driver).double_click(e1).perform()
	# 点击文字
	def click_text(self,text):
		self.driver.find_element_by_link_text(text).click()
	# 关闭当前网页
	def close(self):
		self.driver.close()
	# 退出浏览器
	def kill(self):
		self.driver.quit()
	# 提交
	def sublimit(self,*ele):
		self.element_wait(*ele)
		e1=self.element(*ele)
		e1.sublimit()
	# 刷新当前页面
	def f5(self):
		self.driver.refresh()
	# 执行js
	def js(self,sprit):
		self.driver.execute_script(sprit)
	#获取
	def get_attribute(self,attribute,*ele):
		e1=self.element(*ele)
		return e1.get_attribute(attribute)
	#获取元素文字
	def get_text(self,*ele):
		self.element_wait(*ele)
		e1=self.element(*ele)
		return e1.text
	#判断是否可点击
	def get_is_dis(self,*ele):
		self.element_wait(*ele)
		e1=self.element(*ele)
		return e1.is_displayed()
	# 获取title
	def get_title(self):
		return self.driver.title
	# 截屏
	def get_screen(self,file_path):
		self.driver.get_screenshot_as_file(file_path)
	# 隐式等待
	def wait(self):
		self.driver.implicitly_wait(10)
	# 接受弹窗
	def accpet(self):
		self.driver.switch_to.alert.accept()
	#关闭弹窗
	def dismiss_alert(self):
		self.driver.switch_to.alert.dismiss()
	# 切换到frame
	def switch_to_frame(self,*ele):
		self.element_wait(*ele)
		if1=self.element(*ele)
		self.driver.switch_to.frame(if1)
	#从frame切换回
	def switch_to_content(self):
		self.driver.switch_to.default_content()
	#两个窗口中切换另一个窗口
	def switch_to_win(self):
		for winname in self.driver.window_handles:
			if winname!=self.driver.current_window_handle:
				self.driver.switch_to.window(winname)
if __name__=="__main__":
	pass
