from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import os





def get_url (urls):
    # deleting file 
    try :
        os.remove("urls_to_scrap.txt")

    except FileNotFoundError:
        print('File not found')
    # defnitons 
    product = input("Which item do you want to compare prices for?")
    options = Options()

    #web- settings
    options.add_argument("--headless")
    options.add_argument("--inprivate")  
    driver = webdriver.Edge(options=options)

    #web- functions 
    for url in urls:

        driver.get(url)
        if url == "https://flamberg.com.pl":
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='text' and @placeholder='Wpisz czego szukasz']"))
                )
            search_box.send_keys(product)
            search_box.send_keys(Keys.RETURN)
            current_url = driver.current_url 

            #list- appending url to file
            with open ("urls_to_scrap.txt", "a",encoding= 'utf-8') as f:
                f.write(current_url+ "\n")
        elif url == 'https://strefamtg.pl':
            search_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, "s")))
            search_box.send_keys(product)
            search_box.send_keys(Keys.RETURN)
            current_url = driver.current_url 

            #list- appending url to file
            with open ("urls_to_scrap.txt", "a",encoding= 'utf-8') as f:
                f.write(current_url + "\n")

        
    print("urls added sucefuly")




