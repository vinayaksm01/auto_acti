import time
from constants import constants as cs
class report:
    def __init__(self,driver):
        self.driver=driver
        self.click_report="//*[@class='content reports']"
        self.click_create_chart="(//*[@class='i'])[1]"
        self.click_add_dash="(//*[@class='addToDashboard'])[1]"
        self.add_name_to_dash="(//*[@class='reportNameEdit inputFieldWithPlaceholder'])[1]"
        self.click_save="(//*[@class='buttonIcon'])[1]"
        self.click_close="//*[@id='closeCreateChartLightboxButton']"
        self.click_on_new_report="(//*[@class='i'])[2]"
        self.click_on_staff_perf="//*[@id='reportName_1']"
        self.click_close_report="//*[@id='createReportLightBox_closeLightbox']"
        self.click_config_rpt="//*[@id='configureReportParametersButton']"
        self.export_rpt="//*[@id='csvPreviewTab']"
        self.click_export_csv_rpt="//*[@id='genCSVReportConfiguration']"
        self.close_the_csv_rpt="//*[@id='cancelReportConfiguration']"
    def click_on_rept(self):
        self.driver.find_element_by_xpath(self.click_report).click()

    def click_on_create_chart(self):
        self.driver.find_element_by_xpath(self.click_create_chart).click()
        time.sleep(8)
    def add_usr(self):
        self.driver.find_element_by_xpath(self.click_add_dash).click()
    def add_dash_name(self):
        self.driver.find_element_by_xpath(self.add_name_to_dash).send_keys(cs.cur_time)
        self.driver.find_element_by_xpath(self.click_save).click()
        self.driver.find_element_by_xpath(self.click_close).click()
    def new_report(self):
        self.driver.find_element_by_xpath(self.click_on_new_report).click()
        self.driver.find_element_by_xpath(self.click_on_staff_perf).click()

    def click_config_report(self):
        self.driver.find_element_by_xpath(self.click_config_rpt).click()
        time.sleep(8)
        self.driver.find_element_by_xpath(self.export_rpt).click()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.click_export_csv_rpt).click()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.close_the_csv_rpt).click()