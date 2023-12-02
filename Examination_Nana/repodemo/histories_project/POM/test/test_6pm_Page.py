import pytest


@pytest.mark.usefixtures('get_driver')
class TestProductTypeTextAssertion():
    def test_assert_product_type_text(self):
       # self.homepage.click_on_number_link()
       self.homepage.click_on_womans_shop()
       self.womanpage.select_bags_element()
       # self.womanpage.is_bag_selected()
       # self.womanpage.bag_tag_displayed()
       # self.womanpage.find_bag_tag()
       self.womanpage.assert_bags_item_is_selected()

"""1. Navigate to https://www.6pm.com/
2. Click on the 1-888-676-2660
3. Close opened alert
4. Click on Shop Women's Sale section, Select product type from Product Type, which is in the left side of the page and 
Assert selected product type
5. * Assert selected tag text under "Your Selections" text
"""

"""No need to check with seperate method locator is displayed
or create method just finding element,
also when you are taking text from element in the DOM
should be a text under the tag where your locator is
I've corrected on Womans_products page
structure is good, that's why your score is 43
"""