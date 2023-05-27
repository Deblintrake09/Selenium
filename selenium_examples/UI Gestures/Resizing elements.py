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

driver.get("https://jqueryui.com/resources/demos/resizable/default.html")
driver.implicitly_wait(1)

resizable = driver.find_element(By.CSS_SELECTOR, '#resizable')

ActionChains(driver).drag_and_drop_by_offset(resizable, 400, 400).perform()
