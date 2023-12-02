

from Ani.ExamHani.examtemplate.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By


class HomePage(Helpers):
    accessories=(By.XPATH,"(//*[@id='root'']/div[1]/div[1]/header/div[2]/ul/li[4]/a)")

    def click_on_accessories(self):
        self.find_and_click(self.click_on_accessories)
