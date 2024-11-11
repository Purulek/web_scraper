import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By



def open_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.text, 'html.parser')
        price_elements = soup.find_all(['strong', 'span', 'div'], class_=True)
        for element in reversed(price_elements):
                price_text = element.get_text(strip=True)
                if "projector_shipping__price" in element.get("class", []):
                    pass

                elif any(currency in price_text for currency in ["$", "zł", "€", "PLN"])and price_text[0].isdigit():
                    print(f"price: {price_text}")
                    break
    else: 
        print("URL dosent work")
                                                





    
open_website("https://flamberg.com.pl/pl/products/warhammer-40000-adepta-sororitas-aestred-thurga-reliquant-at-arms-189587")
with open ("urls_to_scrap",'r',encoding= 'utf-8') as file:
    for url in file.readlines():
        open_website(url)
