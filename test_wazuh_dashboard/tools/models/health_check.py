from selenium.webdriver.common.by import  By
from test_wazuh_dashboard.tools.common import CommonOps
from test_wazuh_dashboard.tools import BASE_URL

class HealthCheckPage(CommonOps):

    URL = BASE_URL + '/app/wazuh#/health-check'
    HEALTH_CHECK_FORM = (By.XPATH, '//react-component[@name="HealthCheck"]')
    ERROR_MESSAGE = (By.XPATH, '//react-component/div/div[3]/div/span')
    API_RELOAD_BUTTON = (By.XPATH, '//react-component/div/div[1]/dl/dd[1]/p/span[3]/button')

    def get_url(self):
        return self.URL

    def get_healthcheck_form(self):
        self.wait_for(self.HEALTH_CHECK_FORM)

    def click_api_reload_button(self):
        self.wait_for(self.API_RELOAD_BUTTON).click()

    def get_error_message(self):
        return self.wait_for(self.ERROR_MESSAGE)
