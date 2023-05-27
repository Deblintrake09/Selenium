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

driver.get("http://deluxe-menu.com/popup-mode-sample.html")
driver.implicitly_wait(1)

image = driver.find_element(By.XPATH, '//table[1]/tbody/tr/td[3]/p[2]/img')
ActionChains(driver).context_click(image).perform()
ActionChains(driver).move_to_element(driver.find_element(By.ID, 'dm2m1i1tdT')).perform()
ActionChains(driver).move_to_element(driver.find_element(By.ID, 'dm2m2i1tdT')).perform()
ActionChains(driver).click(driver.find_element(By.ID, 'dm2m3i1tdT')).perform()

