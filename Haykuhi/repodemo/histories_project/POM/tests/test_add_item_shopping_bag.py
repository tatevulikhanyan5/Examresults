
from Haykuhi.repodemo.histories_project.POM.tests.base_test import BaseTest


class TestAddItemShoppingBagAndAssertText(BaseTest):
    def test_add_shopping_bag_item(self):
        self.navigate_products_page_add_shopping_bag_button_assert_text()

"""1. Navigate to https://www.6pm.com/
2. Click on the CLEARENCE
3. Click on the first result
4. Click on the add to shipping bug button and assert text of add to shipping bug button.
5. * Select size and check item added to the shipping bug
"""

"Very good Haykuhi jan, your score is 50"