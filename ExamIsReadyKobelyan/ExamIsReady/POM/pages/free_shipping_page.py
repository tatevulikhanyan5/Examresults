from ExamIsReadyKobelyan.ExamIsReady.POM.lib.helpers import Helpers
from ExamIsReadyKobelyan.ExamIsReady.POM.lib.assertions import assert_that
from selenium.webdriver.common.by import By

class FreeShippingPageFunctionality(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    first_header_text = (By.CLASS_NAME, "xa-z")

    def assert_first_header_text(self):
        actual_text = self.find(self.first_header_text,get_text=True)
        assert_that(actual_text,"Shipping and Delivery Questions")

    def go_to_main_page(self):
        self.go_to_backwards()