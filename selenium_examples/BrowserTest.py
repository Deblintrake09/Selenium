from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = "firefox"

if browser == "chrome":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
elif browser == 'firefox':
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe");
    driver = webdriver.Firefox(firefox_binary=binary, executable_path=GeckoDriverManager().install())
else:
    driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

driver.get("http://way2automation.com")
driver.maximize_window()

title = driver.title

print("Page title: " + title)

assert "Selenium" in title

driver.close()
driver.quit()