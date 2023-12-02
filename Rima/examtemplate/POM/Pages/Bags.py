from selenium.webdriver.common.by import By

from Rima.examtemplate.POM.lib.helpers import Helpers


class Bags(Helpers):
    first_item = (By.CLASS_NAME, 'ida-z')
    bags_text = (By.XPATH, '//*[@id="searchSelectedFilters"]/li[1]')

    def click_on_first_item(self):
        self.find_and_click(self.first_item)

    def assert_bags(self, bags_text='Bags'):
        actual_text = self.find(self.bags_text, get_text=True)
        assert actual_text == bags_text
