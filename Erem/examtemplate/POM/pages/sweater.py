from Erem.examtemplate.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By

class HomePageFunctionality(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    home_page_sweater_btn=(By.CLASS_NAME, 'sweater')


    def click_on_home_page_sweater_btn(self):
        self.find_and_click(self.home_page_sweater_btn)