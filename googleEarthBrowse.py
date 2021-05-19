from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
driver.get("https://www.google.com/earth/")
driver.maximize_window() # NB: do this most of the time to see all elements.
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
# Condition above: click the button when it shows up on the browser.
launchEarthButton.click()