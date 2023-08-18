from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://quotes.toscrape.com/login')

WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'username')))

login = driver.find_element(By.XPATH, "//input[@id='username']")
password = driver.find_element(By.XPATH, "//input[@id='password']")

login.send_keys('admin')
password.send_keys('admin')

login_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
login_btn.click()
WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, 'quote')))

html = driver.page_source
print(html)

#driver.quit()