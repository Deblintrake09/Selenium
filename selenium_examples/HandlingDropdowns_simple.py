from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())

driver.get("http://echoecho.com/htmlforms11.htm")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# Selecting dropdown by visible name
driver.find_element(By.NAME, 'dropdownmenu').send_keys("Milk")