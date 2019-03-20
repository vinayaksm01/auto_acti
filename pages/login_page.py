from constants import constants as cs
class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.un_txt_fld_id="username"
        self.pwd_txt_fld_name="pwd"
        self.login_btn_id="loginButton"

    def enter_un(self,un):
        self.driver.find_element_by_id(self.un_txt_fld_id).send_keys(cs.UN)

    def enter_pwd(self,pwd):
        self.driver.find_element_by_name(self.pwd_txt_fld_name).send_keys(cs.PWD)

    def click_on_login_btn(self):
        self.driver.find_element_by_id(self.login_btn_id).click()
