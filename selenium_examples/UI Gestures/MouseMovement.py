from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://way2automation.com")
driver.implicitly_wait(1)

menu = driver.find_element(By.XPATH, '//*[@id="menu-item-27597"]')

action = ActionChains(driver)
action.move_to_element(menu).perform()
driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div/nav/div/ul/li[3]/ul/li[9]/a').click()

