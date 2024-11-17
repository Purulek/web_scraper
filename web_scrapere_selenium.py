from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options



product = input("Which item do you want to compare prices for?")
options = Options()
#options.add_argument("--headless")
options.add_argument("--inprivate")  
driver = webdriver.Edge(options=options)

driver.get("https://flamberg.com.pl/")
search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='text' and @placeholder='Wpisz czego szukasz']"))
    )




search_box.send_keys(product)
search_box.send_keys(Keys.RETURN)


current_url = driver.current_url



with open ("urls_to_scrap", "w+",encoding= 'utf-8') as f:
    f.write(current_url)




