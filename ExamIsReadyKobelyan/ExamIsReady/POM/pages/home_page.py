from ExamIsReadyKobelyan.ExamIsReady.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By

class HomePageFunctionality(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    home_page_free_shipping_link_btn=(By.CLASS_NAME, "wj-z")
    search_field_btn = (By.ID, "searchAll")

    def click_on_free_shipping_link_btn(self):
        self.find_and_click(self.home_page_free_shipping_link_btn)

    def search_for_dresses_in_search_field(self):
        self.find_and_send_keys(self.search_field_btn,"dresses")
