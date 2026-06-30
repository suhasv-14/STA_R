from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.demoblaze.com/")

time.sleep(3)

products = driver.find_elements(By.CLASS_NAME,"hrefch")

flag=False

for product in products:
    if product.text=="XYZ Mobile":
        flag=True

if flag:
    print("FAIL")
else:
    print("PASS : Product Not Available")

driver.quit()