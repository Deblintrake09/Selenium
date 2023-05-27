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

driver.get("https://jqueryui.com/resources/demos/slider/default.html")
driver.implicitly_wait(1)

slider = driver.find_element(By.CSS_SELECTOR, '#slider')
size = slider.size
width, height = size['width'], size['height']

ActionChains(driver).drag_and_drop_by_offset(slider, width/2, 0).perform()
