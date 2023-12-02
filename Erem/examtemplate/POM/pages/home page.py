from Erem.examtemplate.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By

class HomePageFunctionality(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    home_page_login_btn=(By.CLASS_NAME, "ia-z")


    def click_on_home_page_login_btn(self):
        self.find_and_click(self.home_page_login_btn)

    def assert_home_page_login_btn(self,header_text='Your primary account information'):
        actual_text=self.find(self.home_page_login_btn,get_text=True)
        actual_text==header_text