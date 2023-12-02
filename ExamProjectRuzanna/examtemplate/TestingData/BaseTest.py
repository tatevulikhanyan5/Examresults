import pytest


@pytest.mark.usefixtures('get_driver')
class BaseTest:

    def click_my_bag_than_home_page(self):
        self.homepage.click_on_my_bag_icon()
        self.mybagpage.assert_mybag_icon_text()
        # self.mybagpage.assert_home_page_icon_text()
        self.mybagpage.click_on_home_page()
        self.mybagpage.assert_home_page_icon_text()
        self.mybagpage.driver_back()
        self.mybagpage.assertion_tag_text()

    """
1. Navigate to https://www.6pm.com/
2. Click on the My Bag icon
3. Assert My Bag text on the modal
4. Click on Home Page link on the modal and assert Home page text in the page
5. * Check selected tag under "Your Selections" part"""

