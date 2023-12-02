
from selenium.webdriver.common.by import By
from ExamProjectRuzanna.examtemplate.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By


class HomePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    my_bag_icon = (By.CLASS_NAME, 'ta-z')

    def click_on_my_bag_icon(self):
        self.find_and_click(self.my_bag_icon)



