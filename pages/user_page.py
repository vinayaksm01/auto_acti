import time
class user:
    def __init__(self,driver):
        self.driver = driver
        self.click_user="//*[@class='content users']"
        self.click_on_user="(//*[@class='userNameContainer'])[2]"
        self.close_user="//*[@id='closeUserDataLightBoxBtn']"
    def clk_user(self):
        self.driver.find_element_by_xpath(self.click_user).click()
        time.sleep(8)
        self.driver.find_element_by_xpath(self.click_on_user).click()
        time.sleep(8)
        self.driver.find_element_by_xpath(self.close_user).click()
        time.sleep(8)