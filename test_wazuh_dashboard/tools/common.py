from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def handle_cert_authority_screen(driver):
    if driver.find_element(By.ID, 'error-code') is not None:
        if 'NET::ERR_CERT_AUTHORITY_INVALID' in driver.find_element(By.ID, 'error-code').text:
            driver.find_element(By.ID, 'details-button').click()
            driver.find_element(By.ID, 'proceed-link').click()


class CommonOps:
    '''
        This class abstracts the basic operations for a driver.
    '''
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)
