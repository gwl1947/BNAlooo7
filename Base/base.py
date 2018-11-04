from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver =driver
    def base_find(self,loc):
        return WebDriverWait(self.driver,timeout=30,poll_frequency=0.5).until(lambda x: x.find_element("//*[contains(*loc)]") )
    # com.yunmall.lc / com.yunmall.ymctoc.ui.activity.MainActivity
    def base_click(self,loc):
        self.base_find(loc).click()
    def base_input(self,loc,text):
        a=self.base_find(loc)
        a.clear()
        a.send_keys(text)