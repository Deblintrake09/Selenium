from selenium.webdriver.common.by import By


def handle_cert_authority_screen(driver):
    if driver.find_element(By.ID, 'error-code') is not None:
        if 'NET::ERR_CERT_AUTHORITY_INVALID' in driver.find_element(By.ID, 'error-code').text:
            driver.find_element(By.ID, 'details-button').click()
            driver.find_element(By.ID, 'proceed-link').click()
