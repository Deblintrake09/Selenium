import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from test_wazuh_dashboard.tools import BASE_URL, DASHBOARD_USER, DASHBOARD_PASS
from test_wazuh_dashboard.tools.common import handle_cert_authority_screen
from test_wazuh_dashboard.tools.models.login_page import LoginPage


@pytest.fixture()
def driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--start-maximized')

    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


@pytest.fixture()
def close_driver(driver):
    yield
    driver.quit()


@pytest.fixture()
def perform_dashboard_login(driver, close_driver):

    # Open URL
    driver.get(BASE_URL)
    driver.implicitly_wait(1)

    handle_cert_authority_screen(driver)

    # Define LoginPage Object
    form = LoginPage(driver)

    # Check LoginForm exists
    form.get_login_form()

    # Enter username, password and click login button
    form.enter_username(DASHBOARD_USER)
    form.enter_password(DASHBOARD_PASS)
    form.click_login_button()
