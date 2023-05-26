from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

driver = uc.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://gmail.com")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)


# driver.find_element(By.ID, "identifierId").send_keys("andres.micalizzi.casali@gmail.com")
# driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("andres.micalizzi.casali2@gmail.com")
driver.find_element(By.CSS_SELECTOR, '#identifierId').send_keys("andres.micalizzi.casali@gmail.com")

driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()

element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
element.send_keys("password")
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()

error_message = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[2]/div[2]/span').text
print(str(error_message))