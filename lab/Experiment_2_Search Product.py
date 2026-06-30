from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.demoblaze.com/")

time.sleep(3)

driver.find_element(By.LINK_TEXT,"Samsung galaxy s6").click()

time.sleep(3)

if "Samsung galaxy s6" in driver.page_source:
    print("PASS : Product Found")
else:
    print("FAIL")

driver.quit()