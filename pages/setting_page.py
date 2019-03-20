import time
from constants import constants as cs
from selenium.webdriver.support.select import Select
class setting:
    def __init__(self,driver):
        self.driver=driver
        self.click_on_setting="(//*[@class='popup_menu_label'])[1]"
        self.click_on_work_schedule="//*[text()='Types of Work']"
        self.click_on_type_wrk="//*[text()='Create Type of Work']"
        self.click_name="//*[@id='name']"
        self.create_type_work="//*[@type='submit']"

    def click_on_stg(self):
        self.driver.find_element_by_xpath(self.click_on_setting).click()
        time.sleep(8)
        self.driver.find_element_by_xpath(self.click_on_work_schedule).click()
        time.sleep(8)
    def click_type_of_work(self):
        self.driver.find_element_by_xpath(self.click_on_type_wrk).click()
        time.sleep(8)
        self.driver.find_element_by_xpath(self.click_name).send_keys(cs.cur_time)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.create_type_work).click()
