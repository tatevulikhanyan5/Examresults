from Erem.examtemplate.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By

"""1. Navigate to https://www.6pm.com/
2. Click on the icon for login
3. Assert "Your Primary Account Information" text on the page
4. Go to back with browser and search "sweaters" in the search input field
5. * From Sort By DDL select Newest"""

class NewestPageFunctionality(Helpers):
    def __init__(self, driver):
        super().__init__(driver)

    newest_page_btn=(By.CLASS_NAME, "xR-z")


    def click_on_newest_page_btn(self):
        self.find_and_click(self.newest_page_btn)

# (By.CLASS_NAME, "class="xR-z") class in not needed, I've corrected

"""test is not created, so fully not completed
your score is 30"""

