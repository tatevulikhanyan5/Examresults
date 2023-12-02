import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_to_accessories_page(self):
        self.homePages.click_on_accessories()

    def navigate_to_hats(self):
        self.accessoriespages.click_on_hats()


    def select_checkbox(self):
        self.hatspages.check_checkbox()

    def text_check(self):
        self.hatspages.assert_text
