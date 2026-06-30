from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.demoblaze.com/")

time.sleep(3)

driver.find_element(By.LINK_TEXT,"Samsung galaxy s6").click()

time.sleep(3)

driver.find_element(By.LINK_TEXT,"Add to cart").click()

alert = WebDriverWait(driver,10).until(EC.alert_is_present())

print(alert.text)

alert.accept()

driver.quit()