

from selenium.webdriver.common.by import By
from Haykuhi.repodemo.histories_project.POM.lib.helpers import Helpers


class AddShoppingBag(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    add_shopping_bag_button = (By.ID, 'add-to-cart-button')

    def click_on_add_shopping_bag_button(self):
        self.find_and_click(self.add_shopping_bag_button)

