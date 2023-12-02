from Ani.ExamHani.examtemplate.POM.Tests import BaseTest


class TestExam(BaseTest):
    def test_filter_text(self):
     self.navigate_to_accessories_page()
     self.navigate_to_hats()
     self.select_checkbox()
     # self.text_check

"""1. Navigate to https://www.6pm.com/
2. Click on the Accessories
3. Click on the Hats section 
4. Click on the first Brand checkbox in the left part of the page  and assert "Your Selections" text on the page
5.* Check that correct brand is selected"""

"""1.Structure is correct,
 but you inherit helpers file not the class
class AccPage(helpers): should be class AccPage(Helpers):
 request.cls.homePages = HomePage(driver) same in the conftest
 you should import class name (Ani.ExamHani.examtemplate.POM.pages.HomePage import HomePage)
 not page from Ani.ExamHani.examtemplate.POM.pages import HomePage
 because object creation we are doing from class
 2. also not robust locators, try to find yourself
 so your score is 38
 """