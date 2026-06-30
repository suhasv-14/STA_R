from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.demoblaze.com/")

driver.find_element(By.ID,"login2").click()

time.sleep(2)

driver.find_element(By.ID,"loginusername").send_keys("testuser")

print("PASS : Username Entered Successfully")

driver.quit()