from constants import constants as cs
class Logout:
    def __init__(self,driver):
        self.driver=driver
        self.logout_lnk_id="logoutLink"

    def click_on_logout_link(self):
        self.driver.find_element_by_id(self.logout_lnk_id).click()