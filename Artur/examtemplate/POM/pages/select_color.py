from selenium.webdriver.common.by import By
from Artur.examtemplate.POM.lib.helpers import Helpers

"""1. Navigate to https://www.6pm.com/
2. Click on the SHOP THE SALE
3. Click on the one of the  Genders from the Gender part, which is in the left side of the page
4. Select one of the colors from Color part,  which is in the left side of the page and assert "Your Selections" text on the page
5.* Check that first item color is selected color"""

class ColorPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    color_btn = (By.CLASS_NAME, 'Black')

    def click_on_color_btn(self):
        color_btn_txt = self.find(By.CLASS_NAME, get_text=True)
        assert color_btn_txt == "Black"
        self.find_and_click(self.color_btn)

    def assert_click_on_color_btn(self, header_text='Black'):
        actual_text = self.find(self.click_on_color_btn, get_text=True)
        assert actual_text == header_text


"""  color_btn_txt = self.find(By.CLASS_NAME, get_text=True)
     here you should give locator color_btn instead of By.CLASS_NAME
       actual_text = self.find(self.click_on_color_btn, get_text=True)
      here you give method name instead of locator
       test is missing, no objects created on conftest
       so your score is 30"""

