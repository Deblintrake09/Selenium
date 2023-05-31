from selenium.webdriver.common.by import By
from test_wazuh_dashboard.tools.common import CommonOps


class LoginPage(CommonOps):

    FORM_LOCATOR = (By.CLASS_NAME, 'euiForm')
    FORM_USERNAME = (By.CSS_SELECTOR, '.euiFieldText.euiFieldText--inGroup[placeholder=Username]')
    FORM_PASSWORD = (By.CSS_SELECTOR, '.euiFieldText.euiFieldText--inGroup[placeholder=Password]')
    FORM_LOGIN_BTN = (By.CSS_SELECTOR, '.euiButton__text')
    ERROR_MESSAGE = (By.XPATH, '//form/div[4]/div/div/b')

    def get_login_form(self):
        self.wait_for(self.FORM_LOCATOR)

    def enter_username(self, username):
        self.wait_for(self.FORM_USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait_for(self.FORM_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.wait_for(self.FORM_LOGIN_BTN).click()

    def get_login_error_message(self):
        return self.wait_for(self.ERROR_MESSAGE).text
