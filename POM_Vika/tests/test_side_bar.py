from POM_Vika.tests.base_test import BaseTest


class TestSideBar(BaseTest):
    def test_filtering_by_price(self):
        self.navigate_to_shop_now_page()
        self.verify_filtering_by_price()

"""
1. Navigate to https://www.6pm.com/
2. Click on the Shop Now link
3. Search 35 in the Price search part, which is in the left side of the page
4. Check the checkbox  and assert Your Selections text in the page
5.* Check that first item price is smaller than 36
"""

"""Good job
Only check my comment in side_bar.py
Your score is 49"""
