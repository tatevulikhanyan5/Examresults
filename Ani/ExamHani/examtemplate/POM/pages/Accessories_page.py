from Ani.ExamHani.examtemplate.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By


class AccPage(Helpers):
    hats = (By.XPATH, "(//*[@id='main']/div/div/div[2]/div/div[2]/div/div[4]/article/a})")

    def click_on_hats(self):
        self.find_and_click(self.click_on_hats)
