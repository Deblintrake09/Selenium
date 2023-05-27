from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())

driver.get("http://wikipedia.com")
driver.maximize_window()
driver.implicitly_wait(1)

# Selecting dropdown by visible name
dropdown = driver.find_element(By.ID, 'searchLanguage')
select = Select(dropdown)
select.select_by_visible_text("Eesti")
select.select_by_value("hi")

options = driver.find_elements(By.TAG_NAME, 'option')

for option in options:
    print(f"Text is {option.text}, Language is {option.get_attribute('lang')}")

print( "Total options are " + str(len(options)))