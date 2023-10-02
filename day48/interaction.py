from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://finalproject-client.vercel.app/')

username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')

username.send_keys('monster')
password.send_keys('woofwoof')

submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/form/button[1]')

submit_button.click()



time.sleep(30)

driver.quit()