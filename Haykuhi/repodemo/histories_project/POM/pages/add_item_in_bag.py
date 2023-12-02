

from selenium.webdriver.common.by import By
from Haykuhi.repodemo.histories_project.POM.lib.helpers import Helpers


class AddItemInBag(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    add_item_size = (By.CSS_SELECTOR, 'div[class="Tya-z"]:nth-child(1)')
    bag_item = (By.CLASS_NAME, 'Y-z')

    def click_on_item_size(self):
        self.find_and_click(self.add_item_size)

    def assert_add_shopping_bag_text(self, header_text='1'):
        actual_text = self.find(self.bag_item, get_text=True)
        assert actual_text == header_text