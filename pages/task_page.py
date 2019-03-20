import time

from constants import constants as cs
from selenium.webdriver.support.select import Select
import moment
from selenium import webdriver
class task:
    def __init__(self,driver):
        self.driver=driver
        self.click_view_xpath="//*[@class='content tasks']"
        self.click_add_new="(//*[@class='title ellipsis'])[2]"
        self.click_new_project="//*[@class='item createNewProject ellipsis']"
        self.enter_project_name="//*[@id='projectPopup_projectNameField']"
        self.enter_custmr_name="(//*[@class='x-btn-center'])[1]"
        self.click_cu_name="(//*[@class='x-menu-item-icon '])[5]"
        self.click_create_btn="//*[@id='projectPopup_commitBtn']"


    def click_on_task(self):
        self.driver.find_element_by_xpath(self.click_view_xpath).click()
    def clk_add_new(self):
        self.driver.find_element_by_xpath(self.click_add_new).click()
    def click_on_new_project(self):
        self.driver.find_element_by_xpath(self.click_new_project).click()
    def enter_a_project_name(self):
        self.driver.find_element_by_xpath(self.enter_project_name).send_keys(cs.cur_time)
    def click_enter_cutmr(self):
        self.driver.find_element_by_xpath(self.enter_custmr_name).click()
        self.driver.find_element_by_xpath(self.click_cu_name).click()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.click_create_btn).click()








