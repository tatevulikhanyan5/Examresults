from selenium.webdriver.common.by import By
from Haykuhi.repodemo.histories_project.POM.lib.helpers import Helpers


class Products(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    product_Chaco = (By.CLASS_NAME, 'Tk-z')

    def click_on_product_chaco(self):
        self.find_and_click(self.product_Chaco)
