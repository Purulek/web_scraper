import web_scraper
import web_scrapere_selenium

#urls to scrap
urls = ["https://flamberg.com.pl", 'https://strefamtg.pl']



web_scrapere_selenium.get_url(urls)



with open ("urls_to_scrap.txt",'r',encoding= 'utf-8') as file:
    for url in file.readlines():
        web_scraper.open_website(url)

