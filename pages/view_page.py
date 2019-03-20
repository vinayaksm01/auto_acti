from constants import constants as cs
from selenium.webdriver.support.select import Select
class view:
    def __init__(self,driver):
        self.driver = driver
        self.click_view_xpath="//*[text()='View Time-Track']"
       
    def click_view(self):
        self.driver.find_element_by_xpath(self.click_view_xpath).click()
    # def select_date(self):
    #
    #     day=Select(self.driver.find_element_by_xpath(self.click_date))
    #     day.select_by_visible_text("Previous quarter")
