import requests
from bs4 import BeautifulSoup
import csv


price_classes = [
            "projector_prices__price", 
            "product-price", 
            "price",
            "price-amount",
            "current-price",
            "product-price-value",
            "price price--listing"
        ]



with open ("urls_to_scrap",'r',encoding= 'utf-8') as file:
    for url in file.readline():
        url = url.strip()

        pass


def open_website(url,price_list):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_elements = soup.find_all(['strong', 'span', 'div'], class_=True)
    for element in reversed(price_elements):
            price_text = element.get_text(strip=True)

            if any(currency in price_text for currency in ["$", "zł", "€", "PLN"])and price_text[0].isdigit():
                print(f"price: {price_text}")
                                            





    
open_website("https://flamberg.com.pl/pl/products/warhammer-40000-adepta-sororitas-aestred-thurga-reliquant-at-arms-189587",price_classes)
#response = requests.get("https://strefamtg.pl/chaos-space-marines/106416-chaos-space-marines-chaos-lord-with-jump-pack.html")




"""response = requests.get("https://flamberg.com.pl/pl/products/warhammer-40000-adepta-sororitas-aestred-thurga-reliquant-at-arms-189587")
soup = BeautifulSoup(response.text, 'html.parser')
for price_class in price_classes:
    try:
        products = soup.find('strong', class_= price_class)
        price = products.text.strip()
        print("price: {}".format(price))
    except:
        print("not this class: {}".format(price_class))"""