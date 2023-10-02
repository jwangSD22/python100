from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(url)


cookie = driver.find_element(By.ID,'cookie')
store = driver.find_element(By.ID, 'store')



timer = 0 

while True:
    for _ in range(100):
        cookie.click()
    time.sleep(1)
    timer+=1

    if timer%5 == 0:

        store_items = store.find_elements(By.CSS_SELECTOR,'div')
        grayed = store.find_elements(By.CLASS_NAME,'grayed')
        for item in grayed:
            if store_items.index(item)>=0:
                store_items.remove(item)

        last = store_items[len(store_items)-1]
        last.click()
