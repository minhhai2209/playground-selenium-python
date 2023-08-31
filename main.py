from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
  driver.get("https://discoverflow.co/jamaica/internet-bundles")
  time.sleep(5)

finally:
  driver.quit()