import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def assert_item_name(self):
        self.homepage.search_bags()
        self.bags.click_on_first_item()
        self.bags.assert_bags()
