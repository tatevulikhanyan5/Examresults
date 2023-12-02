import selenium
from selenium.webdriver.common.by import By
from MariaExamProject.examtemplate.POM.lib.helpers import Helpers


class HomePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    under50icon = (By.CLASS_NAME, 'XL-z')

    def click_on_under50icon(self):
        self.find_and_click(self.under50icon)

