from selenium import webdriver
import time


driver = webdriver.Chrome()

url = "https://youtube.com"

driver.get(url)


time.sleep(2)



url = "http://enesco.cf"

driver.get(url)
driver.maximize_window()

print(driver.title)

# if "Enescan Akyüz" in driver.title:
#     driver.save_screenshot("enes.png")

time.sleep(2)

driver.back()

driver.minimize_window()

time.sleep(2)

driver.close()
