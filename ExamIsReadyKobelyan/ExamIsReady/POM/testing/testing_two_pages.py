import time

import pytest
from ExamIsReadyKobelyan.ExamIsReady.POM.lib.helpers import Helpers

@pytest.mark.usefixtures('get_driver')
class TestTwoPagesFunctionality():
    def test_and_assert_that_all_functions_work_properly(self):
        self.home_page.click_on_free_shipping_link_btn()
        self.free_shipping_page.assert_first_header_text()
        self.free_shipping_page.go_to_main_page()
        self.home_page.search_for_dresses_in_search_field()

"""1. Navigate to https://www.6pm.com/
2. Click on the free shipping link
3. Assert "Shipping and Delivery Questions" text on the page
4. Go to back with browser and search dresses in the search input field
5. * Assert selected tags text under "Your Selections" text"""


"""Good job
    Your score is 50"""


