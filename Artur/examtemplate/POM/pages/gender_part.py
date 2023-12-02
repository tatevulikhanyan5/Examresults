from selenium.webdriver.common.by import By
from Artur.examtemplate.POM.lib.helpers import Helpers

class GenderPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    gender_btn = (By.CLASS_NAME, 'Women')

    def click_on_gender_btn(self):
        self.find_and_click(self.gender_btn)