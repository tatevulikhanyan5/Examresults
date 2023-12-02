from Ani.ExamHani.examtemplate.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By


class FirstCheckbox(Helpers):
    checkbox=(By.XPATH, "(//*[@id='searchFilters']/div[1]/div[2]/section[3]/div[2]/ul/li[1]/a)")
    your_selection = (By.XPATH, "(//*[@id='main']/div/div/div/div[4]/div/div/div/div/div/div")

    def check_checkbox(self):
        self.find_and_click(self.check_checkbox())


    def assert_text(self,check_text="Filters were included based on your selections."):
       actual_text=self.find(self.your_selection,get_text=True)
       assert actual_text==check_text