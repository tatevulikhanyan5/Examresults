from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Examination_Nana.repodemo.histories_project.POM.lib.assertions import assert_that
from Examination_Nana.repodemo.histories_project.POM.lib.helpers import Helpers

class WomansPage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    bags = (By.XPATH, '(//*[@class="PE-z"])[1]//li[3]')
    # bag_tag = (By.XPATH, '//*[@id="searchSelectedFilters"]/li/a[1]')
    bag_tag = (By.XPATH, '//*[@href="/women/wAEB4gIBGA.zso?s=recentSalesStyle/desc/"]')
    #or //*[@id="searchSelectedFilters"]/li[1]


    def select_bags_element(self):
        self.find_and_click(self.bags)

    def is_bag_selected(self):
        self.is_selected(self.bags)

    def bag_tag_displayed(self):
        self.is_displayed(self.bag_tag)

    def find_bag_tag(self):
        self.find(self.bag_tag)

    def assert_bags_item_is_selected(self, bag_tag_text = 'Bags'):
        actual_text = self.find(self.bag_tag, get_text=True)
        assert actual_text == bag_tag_text

