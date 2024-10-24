from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)

driver.get("https://orteil.dashnet.org/cookieclicker/")


time.sleep(5)

try:
    language = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
    language.click()
    time.sleep(5)

    cookies = driver.find_element(By.ID, "cookies")
    cookie = driver.find_element(By.ID, "bigCookie")
    prices = driver.find_elements(By.CLASS_NAME, "price")
   

except NoSuchElementException as e:
    print(f"Error finding element: {e}")
    driver.quit()
    exit()

On = True

while On:
    cookie.click()
    cookies_text = cookies.text.split(" ")[0]

    for price in prices:
        price_text = price.text.split(" ")[0]

        try:
            if int(cookies_text.replace(',', '')) >= int(price_text.replace(',', '')):
                driver.execute_script("arguments[0].click();", price)
                break
        except:
            continue

    try:
        upgrade = driver.find_element(By.CLASS_NAME, "crate upgrade enabled")
        upgrade_available = True
    except NoSuchElementException:
        upgrade_available = False

    if upgrade_available:
        try:
            upgrade = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "crate upgrade enabled")))
            driver.execute_script("arguments[0].click();", upgrade)
        except:
            continue
          

