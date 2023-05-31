import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from test_wazuh_dashboard.tools import DASHBOARD_IP, DASHBOARD_PASS, DASHBOARD_USER
from test_wazuh_dashboard.tools.common import handle_cert_authority_screen
from test_wazuh_dashboard.tools.models.login_page import LoginPage


test_cases_data = [(DASHBOARD_USER, DASHBOARD_PASS, True),
                   ('fake_username', DASHBOARD_PASS, False),
                   (DASHBOARD_USER, 'fake_password', False)]


@pytest.mark.parametrize('username, password, isvalid', test_cases_data)
def test_dashboard_login(username, password, isvalid, driver, close_driver):

    # Open URL
    driver.get(f'https://{DASHBOARD_IP}')

    driver.implicitly_wait(1)
    wait = WebDriverWait(driver, 8)

    handle_cert_authority_screen(driver)

    assert driver.title == 'Wazuh', f'Unexpected title found: {driver.title}'

    # Define LoginPage Object
    form = LoginPage(driver)

    # Check LoginForm exists
    form.get_login_form()

    # Enter username, password and click login button
    form.enter_username(username)
    form.enter_password(password)
    form.click_login_button()

    # If credentials are valid, check new page's title, else assert login error message
    if isvalid:
        wait.until(ec.title_contains('Wazuh - Wazuh'))
    else:
        assert 'Invalid username or password. Please try again.' in form.get_login_error_message()
