

from selenium.webdriver.common.by import By
from Haykuhi.repodemo.histories_project.POM.lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    clearance_button = (By.CLASS_NAME, 'Oj-z')

    def click_on_clearance_button(self):
        self.find_and_click(self.clearance_button)



