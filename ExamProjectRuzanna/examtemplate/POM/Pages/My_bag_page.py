from selenium.webdriver.common.by import By
from ExamProjectRuzanna.examtemplate.POM.lib.helpers import Helpers
from ExamProjectRuzanna.examtemplate.POM.lib.assertions import assert_that


class MyBag(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    my_bag_assertion_text = (By.CLASS_NAME, 'Zo-z') #here I've change locator

    def assert_mybag_icon_text(self):
        actual_text = self.find(self.my_bag_assertion_text, get_text=True)
        assert_that(actual_text, 'My Bag')

    my_bag_home_page = (By.XPATH, '/html/body/div[9]/div/div[2]/div[1]/a[2]')

    def click_on_home_page(self):
        self.find_and_click(self.my_bag_home_page)

    home_page_icon_6pm = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/header/div[1]/a/picture/img')
    #here you don't have text in DOM, that's why couldn't find actual text
    #under your finded locator should be text in DOM, so pay
    #attention.. not all elements have text
    def assert_home_page_icon_text(self):
        actual_text = self.find(self.home_page_icon_6pm, get_text=True)
        assert_that(actual_text, '6pm')

    def driver_back(self):
        self.driver_back()

    assertion_of_tag_text = (By.CLASS_NAME, 'href="/null/.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/&si=6081192&sy=1')

    def assertion_tag_text(self):
        actual_text = self.find(self.assertion_of_tag_text, get_text=True)
        assert_that(actual_text, '$50.00 and Under')
