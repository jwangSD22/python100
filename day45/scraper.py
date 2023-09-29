from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.streetfighter.com/6/buckler/ranking/league?character_filter=1&character_id=luke&platform=1&user_status=1&home_filter=2&home_category_id=5&home_id=1&league_rank=24&page=1' 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 

driver.get(url) 
driver.add_cookie({
    "name":"buckler_praise_date","value":"1695945638704"
})
driver.add_cookie({
    "name":"buckler_r_id","value":"ffacf239-a620-4795-aa40-944eb2c851ab"
})
driver.add_cookie({
    "name":"pll_language","value":"en"
})
driver.add_cookie({
    "name":"buckler_id","value":"33RUGpVfr3B_1pmws3z4dtJ0TQ--UK8GWj-E5EtcFl2SL0TAqhLvdvxczzKxUaoS"
})

# Reload the page to apply the cookies
driver.refresh()
# Wait for the page to load completely (you can customize the timeout)


ranking_info = driver.find_element(By.CLASS_NAME, "ranking_ranking_now__last__TghLM")

print(ranking_info.text)

# with open('sf_scrape.html','a',encoding='utf-8') as f:
#     f.write(ranking_info.getText())

driver.quit()





