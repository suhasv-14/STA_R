from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.demoblaze.com/")

time.sleep(2)

driver.find_element(By.ID,"login2").click()

time.sleep(2)

driver.find_element(By.ID,"loginusername").send_keys("YOUR_USERNAME")
driver.find_element(By.ID,"loginpassword").send_keys("YOUR_PASSWORD")

driver.find_element(By.XPATH,"//button[text()='Log in']").click()

time.sleep(5)

welcome = driver.find_element(By.ID,"nameofuser").text

if "Welcome" in welcome:
    print("PASS : Login Successful")
else:
    print("FAIL")

driver.quit()