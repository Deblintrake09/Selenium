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

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.implicitly_wait(1)

draggable = driver.find_element(By.ID, 'draggable')
droppable = driver.find_element(By.ID, 'droppable')

ActionChains(driver).drag_and_drop(draggable, droppable).perform()
