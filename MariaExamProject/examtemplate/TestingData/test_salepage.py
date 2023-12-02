from MariaExamProject.examtemplate.TestingData.Basetest import BaseTest


class TestPages(BaseTest):
    def test_pages_final(self):
        self.clickonsaleThansearch()


"""good job only I've changed method name, because not correct
to use same method name under the method in this case
because you need to use driver_back() method from helpers
in this case it will take the same method from the same file
 def driver_backk(self):
 self.driver_back() ---without return, I've corrected
and also not write test and basetest under testdata, create
seperate test module   
Your score is 48"""

