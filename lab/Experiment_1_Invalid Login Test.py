from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.demoblaze.com/")

driver.find_element(By.ID,"login2").click()

WebDriverWait(driver,10).until(
EC.visibility_of_element_located((By.ID,"loginusername"))
)

driver.find_element(By.ID,"loginusername").send_keys("wrong")

driver.find_element(By.ID,"loginpassword").send_keys("wrong")

driver.find_element(By.XPATH,"//button[text()='Log in']").click()

alert = WebDriverWait(driver,10).until(EC.alert_is_present())

print(alert.text)

alert.accept()

driver.quit()