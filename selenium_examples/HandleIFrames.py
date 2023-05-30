import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_iframe_get")
driver.implicitly_wait(1)

driver.switch_to.frame('iframeResult')
driver.find_element(By.TAG_NAME, 'button').click()



