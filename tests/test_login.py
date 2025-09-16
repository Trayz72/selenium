from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

print("Starting Selenium Demo (Headless Mode)")

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

print("Loading login page...")
driver.get("http://127.0.0.1:5050")
time.sleep(1)


print("Logging in...")
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("secret" + Keys.RETURN)
time.sleep(1)

if "Login successful!" in driver.page_source:
    print("Test Passed! Login successful!")
else:
    print("Test Failed - Login message not found")

driver.quit()
print("Demo Complete!")