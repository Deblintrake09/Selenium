import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_wazuh_dashboard import DASHBOARD_IP, DASHBOARD_PASS, DASHBOARD_USER
from test_wazuh_dashboard.configurations import handle_cert_authority_screen


@pytest.mark.parametrize('username, password, isvalid', [(DASHBOARD_USER, DASHBOARD_PASS, True),
                                                ('fake_username', DASHBOARD_PASS, False),
                                                (DASHBOARD_USER, 'fake_password', False)])
def test_dashboard_login(driver, username, password, isvalid):

    # Open URL
    driver.get(f'https://{DASHBOARD_IP}')
    # Setup wait for later
    wait = WebDriverWait(driver, 8)
    driver.implicitly_wait(1)

    handle_cert_authority_screen(driver)

    assert driver.title == 'Wazuh', f'Unexpected title found: {driver.title}'

    wait.until(lambda d: d.find_element(By.CLASS_NAME, 'euiForm'))

    form_fields = driver.find_elements(By.CSS_SELECTOR, '.euiFieldText.euiFieldText--inGroup')
    form_fields[0].send_keys(username)
    form_fields[1].send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '.euiButtonContent.euiButton__content').click()

    if isvalid:
        wait.until(EC.title_contains('Wazuh - Wazuh'))
    else:
        assert 'Invalid username or password. Please try again.' in driver.find_element(By.XPATH, '//form/div[4]/div/div/b').text

    driver.quit()


