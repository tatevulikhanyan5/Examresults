
from selenium.webdriver.common.by import By
from Artur.examtemplate.POM.lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    shop_the_sale = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div/div/article/a')

    def click_on_shop_the_sale(self):
        self.find_and_click(self.shop_the_sale)