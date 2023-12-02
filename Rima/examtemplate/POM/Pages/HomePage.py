from selenium.webdriver.common.by import By

from Rima.examtemplate.POM.lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    search_field = (By.ID, 'searchAll')
    submit_button = (By.CLASS_NAME, 'oa-z')

    def search_bags(self):
        self.find_and_send_keys(self.search_field, "bags")
        self.find_and_click(self.submit_button)

