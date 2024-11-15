from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import requests



options = Options()
options.add_argument("--headless")
options.add_argument("--inprivate")  
driver = webdriver.Edge(options=options)

driver.get("https://strefamtg.pl")
search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "s"))
    )

search_box.send_keys("Thousand Sons Magnus the Red")
search_box.send_keys(Keys.RETURN)


current_url = driver.current_url



with open ("urls_to_scrap", "w+",encoding= 'utf-8') as f:
    f.write(current_url)




