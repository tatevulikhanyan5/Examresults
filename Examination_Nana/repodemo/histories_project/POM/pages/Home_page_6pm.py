from selenium.webdriver.common.by import By

from Examination_Nana.repodemo.histories_project.POM.lib.helpers import Helpers

class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    # number_link = (By.XPATH, '//*[@class="da-z"]')
    #
    #
    # def click_on_number_link(self):
    #     self.find_and_click(self.number_link)

    shop_womans_sale_btn = (By.XPATH, '(//*[@class="ZL-z bM-z"])[2]')

    def click_on_womans_shop(self):
        self.find_and_click(self.shop_womans_sale_btn)

