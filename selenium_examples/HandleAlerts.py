import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.implicitly_wait(1)

driver.find_element(By.XPATH, '//div/input[2]').click()

alert = Alert(driver)

print(f'Alert text : {alert.text}')
time.sleep(3)
alert.accept()
