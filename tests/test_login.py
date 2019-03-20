from selenium import webdriver
import pytest
import allure
import time
import moment
from selenium.webdriver.common.keys import Keys
from pages.view_page import view
from pages.login_page import LoginPage
from pages.landing_page import Logout
from constants import constants as cs
from pages.task_page import task
from pages.report_page import report
from pages.user_page import user
from pages.setting_page import setting
class TestLogin:
    @pytest.fixture(scope="session")
    def test_setup(self):
        global driver
        driver=webdriver.Chrome(executable_path="C:/Users/chethan.R/PycharmProjects/auto_acti/drivers/chromedriver.exe")
        time.sleep(5)
        driver.get(cs.URL)
        driver.maximize_window()
        login = LoginPage(driver)
        login.enter_un(cs.UN)
        login.enter_pwd(cs.PWD)
        login.click_on_login_btn()
        time.sleep(5)
        # yield
        #
        # home = Logout(driver)
        # home.click_on_logout_link()
        # time.sleep(5)
        # driver.quit()

    def test_click_view(self,test_setup):
        view_time=view(driver)
        time.sleep(15)
        view_time.click_view()
        time.sleep(8)

    def test_click_task(self,test_setup):
        ts=task(driver)
        ts.click_on_task()
        time.sleep(5)
        ts.clk_add_new()
    def test_create_project(self,test_setup):

        ts=task(driver)
        ts.click_on_new_project()
        time.sleep(10)
        ts.enter_a_project_name()
        time.sleep(10)
        ts.click_enter_cutmr()
        time.sleep(10)
    def test_clik_rpt(self,test_setup):
        rpt=report(driver)
        rpt.click_on_rept()
        time.sleep(10)

        rpt.click_on_create_chart()
        rpt.add_usr()
        rpt.add_dash_name()
    def test_click_new_report(self,test_setup):
        nw_rpt = report(driver)
        nw_rpt.new_report()
        time.sleep(10)

    def test_congig_rpt_gen(self,test_setup):
        rpt_gen=report(driver)
        rpt_gen.click_config_report()
    def test_usr(self,test_setup):
        usr=user(driver)
        usr.clk_user()

    def test_setting(self,test_setup):
        acti_setting=setting(driver)
        acti_setting.click_on_stg()
    def test_type_work(self,test_setup):
        type_work=setting(driver)
        type_work.click_type_of_work()
    def test_logout(self,test_setup):
        home = Logout(driver)
        home.click_on_logout_link()
        time.sleep(5)
        driver.quit()







