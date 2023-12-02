import pytest

@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_products_page_add_shopping_bag_button_assert_text(self):
        self.homepage.click_on_clearance_button()
        self.products.click_on_product_chaco()
        self.add_item_bag.click_on_item_size()
        self.add_shopping_bag.click_on_add_shopping_bag_button()
        self.add_shopping_bag.assert_add_shopping_bag_text()

