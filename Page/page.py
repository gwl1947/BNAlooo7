import Base
from Base.base import Base
import Page
class Page(Base):
    def page_input_username(self,username):
        self.base_input(Page.dlusername,username)
    def page_input_password(self,password):
        self.base_input(Page.dlpassword,password)
    def page_cick_btn(self,dlbtn):
        self.base_click(dlbtn)