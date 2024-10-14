from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)

driver.get("https://www.amazon.com")