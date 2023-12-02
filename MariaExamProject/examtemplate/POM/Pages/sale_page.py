import selenium
from selenium.webdriver.common.by import By
from MariaExamProject.examtemplate.POM.lib.helpers import Helpers
from MariaExamProject.examtemplate.POM.lib.assertions import assert_that


class SalePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    narrow_choice_icon = (By.CLASS_NAME, 'KE-z')

    def refresh(self):
        self.refresh_page()

    def assert_narrow_choice_icon(self):
        actual_text = self.find(self.narrow_choice_icon, get_text=True)
        assert_that(actual_text, 'Narrow Choices')

    def search_icon(self):
        search_field_icon = (By.CLASS_NAME, 'oa-z')
        self.find_and_click(search_field_icon)
        self.find_and_send_keys(search_field_icon, 'Shoes')

    def driver_backk(self):
        self.go_driver_back()

    tags_text = (By.CLASS_NAME, 'href="/null/.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/&si=6081192&sy=1')

    def assert_tags_text(self):
        actual_text = self.find(self.tags_text, get_text=True)
        assert_that(actual_text, '$50.00 and Under')