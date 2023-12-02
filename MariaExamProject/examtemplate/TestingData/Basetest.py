import time

import pytest

@pytest.mark.usefixtures('get_driver')
class BaseTest:

    def clickonsaleThansearch(self):
        self.homepage.click_on_under50icon()
        self.salepage.refresh()
        self.salepage.assert_narrow_choice_icon()
        self.salepage.search_icon()
        self.selepage.driver_backk()
        time.sleep(2)
        self.salepage.assert_tags_text()
