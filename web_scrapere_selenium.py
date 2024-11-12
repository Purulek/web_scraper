from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests


driver = webdriver.Edge()



driver.get("https://flamberg.com.pl/pl/menu/warhammer-40000-268")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Thousand Sons Magnus the Red")
print(driver.current_url)
search_box.send_keys(Keys.RETURN)
print(driver.current_url)



