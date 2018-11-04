import sys,os
sys.path.append(os.getcwd())
from Base.get_driverr import get_driver
from Page.page import Page
class Test():
    def setup_class(self):
        self.a=Page(get_driver())

    def teardown_class(self):
        self.a.driver.quit()
    def test_01(self,username="123456",password="aaaaa"):
        self.a.page_input_username(username)
        self.a.page_input_password(password)
        self.a.page_cick_btn()


