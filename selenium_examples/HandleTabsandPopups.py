import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open URL
driver.get("https://www.lambdatest.com/selenium-playground/window-popup-modal-demo")

# Setup wait for later
wait = WebDriverWait(driver, 10)

# Store the ID of the original window
original_window = driver.current_window_handle

# Check we don't have other windows open already
assert len(driver.window_handles) == 1

# Click the link which opens in a new window
driver.find_element(By.XPATH, "//section[4]/div/div/div[2]/div[1]/a[1]").click()

# Wait for the new window or tab
wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Wait for the new tab to finish loading content
wait.until(EC.title_is("Twitter"))
