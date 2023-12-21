import requests
import time
from lxml.etree import HTML
import csv
import re
from requests import get

def scrape_and_save_data(initial_query, time_limit=60, return_format='csv'):

   cookies = {
    'ARRAffinity': '667d9ee9de5abee7473f2841dda6efd732f47b01481206fe0e6986367eff378b',
    'ARRAffinitySameSite': '667d9ee9de5abee7473f2841dda6efd732f47b01481206fe0e6986367eff378b',
    '.Nop.Customer': '84370d86-823f-4860-a621-b9e86c954aa0',
    '.Nop.Antiforgery': 'CfDJ8LXhlGhJWyhNjMqsPaDvEXdohlhTlHDGiQiELmOtnqZ2bYIxNU3L2ducdyVXbBFJML5U2-0HsinoCOrh69Q6JC6hfXu8n5r5gJYklJuGm7XrQ9qxt_O0z_71uiu8wyFl6B4Cq8Q1vRGJS8sKrH1rNqk',
    '_gcl_au': '1.1.414933568.1702927372',
    '_gid': 'GA1.2.81175552.1702927372',
    '_gat_UA-23705264-1': '1',
    '_scid': '1492d54d-8fc4-4369-8b66-238898e26543',
    '_fbp': 'fb.1.1702927372273.114690513',
    '_ga': 'GA1.2.409492003.1702927372',
    '_scid_r': '1492d54d-8fc4-4369-8b66-238898e26543',
    'cto_bundle': '67xN_V9NUm16QlBuRU5GJTJCTTA3OFA1aUgxQVUlMkZWcGdoUTdra1psZG1GZiUyRjBIVHo1ZXNFZ2tCeFdyaEZpOWxqdjFFbTRiNlhzNG90SG15NU16byUyRlpJbmdqM28xOWd5bUhLeUV6NFh0ZXdTbmJ5RVd2MyUyQm83UU1MQWFHdDMyZWhoamMlMkZwZnQwMEExMDc5ZEJ5YWFkV0thaVZsUzI3Vlk5WFR5TW1HMHhQYlhhZ3FoNkUlM0Q',
    '_ga_S9B50G64P2': 'GS1.1.1702927372.1.1.1702927392.40.0.0',
   }

   headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'ARRAffinity=667d9ee9de5abee7473f2841dda6efd732f47b01481206fe0e6986367eff378b; ARRAffinitySameSite=667d9ee9de5abee7473f2841dda6efd732f47b01481206fe0e6986367eff378b; .Nop.Customer=84370d86-823f-4860-a621-b9e86c954aa0; .Nop.Antiforgery=CfDJ8LXhlGhJWyhNjMqsPaDvEXdohlhTlHDGiQiELmOtnqZ2bYIxNU3L2ducdyVXbBFJML5U2-0HsinoCOrh69Q6JC6hfXu8n5r5gJYklJuGm7XrQ9qxt_O0z_71uiu8wyFl6B4Cq8Q1vRGJS8sKrH1rNqk; _gcl_au=1.1.414933568.1702927372; _gid=GA1.2.81175552.1702927372; _gat_UA-23705264-1=1; _scid=1492d54d-8fc4-4369-8b66-238898e26543; _fbp=fb.1.1702927372273.114690513; _ga=GA1.2.409492003.1702927372; _scid_r=1492d54d-8fc4-4369-8b66-238898e26543; cto_bundle=67xN_V9NUm16QlBuRU5GJTJCTTA3OFA1aUgxQVUlMkZWcGdoUTdra1psZG1GZiUyRjBIVHo1ZXNFZ2tCeFdyaEZpOWxqdjFFbTRiNlhzNG90SG15NU16byUyRlpJbmdqM28xOWd5bUhLeUV6NFh0ZXdTbmJ5RVd2MyUyQm83UU1MQWFHdDMyZWhoamMlMkZwZnQwMEExMDc5ZEJ5YWFkV0thaVZsUzI3Vlk5WFR5TW1HMHhQYlhhZ3FoNkUlM0Q; _ga_S9B50G64P2=GS1.1.1702927372.1.1.1702927392.40.0.0',
    'Referer': 'https://www.gintarine.lt/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }


   def query_to_url(query):
    return f"https://www.gintarine.lt/search?q={query}"
    initial_url = query_to_url(initial_query)
    urls_to_scrape = [initial_url]

    medical_name = []
    medical_price = []
    product_url = []


    response = requests.get(initial_url, cookies=cookies, headers=headers)
    data = HTML(response.text)
    k=0

    product_url.append(initial_url)
#//a[contains(@class, 'paginator__page')]/@href
    for link in data.xpath("//div//a[@class='paginator__item paginator__page']/@data-page"):
      product_url.append(initial_url + '&pagenumber=' + link)
      k=k+1;
#print(product_url)

####

      for url in product_url:
        page_response = requests.get(url, cookies=cookies, headers=headers)
        page_data = HTML(page_response.text)

    # Pavyzdžiui, ieškome prekių pavadinimų (pakeiskite XPath pagal poreikį)
      items = page_data.xpath("//*[@id='product-container']/div[1]/form[17]/div/div[2]/text()")
    #medical_name = data.xpath("//a/img[contains(@class, 'category-grid__title')]/@alt")
    # Apdorojimas arba informacijos saugojimas
      for item in items:
        medical_name.append(item.strip())  # Pridėti teksto apdorojimą, jei reikia
        prices = page_data.xpath("//span[contains(@class, 'product__price--regular')]/text()")

        # Apdorojimas arba informacijos saugojimas
      for price in prices:
        clean_price_match = re.search(r"\d+,\d{2}", price)
        if clean_price_match:
            clean_price = clean_price_match.group()
            # Pakeičiame kablelį į tašką ir konvertuojame į skaičių
            clean_price = float(clean_price.replace(',', '.'))
            #print(clean_price)
        medical_price.append(clean_price)  # Pridėti teksto apdorojimą, jei reikia

    # Išvedamas arba apdorojamas surinktas duomenys


# Išvedamas arba apdorojamas surinktas duomenys
#print(medical_name)
#print(medical_price)
      with open("Medical.csv", encoding='utf-8',mode="w") as file_writer:
        fieldnames=['Pavadinimas', 'Kaina', 'Linkas']
        csv_write = csv.DictWriter(file_writer, fieldnames, delimiter = ',')
        csv_write.writeheader()
    #csv_write.writerow
    #print({"Pavadinimas",   "Kaina"      , "Linkas" })
        for i in range(k):
          print({"Pavadinimas": medical_name[i], "Kaina": medical_price[i], "Linkas": product_url[i]})
          #clean_price_match[i] = re.search(r"\d+,\d{2}", medical_price[i])
          csv_write.writerow({"Pavadinimas": medical_name[i], "Kaina": medical_price[i], "Linkas": product_url[i]})

if __name__=="__main__":
   initial_query = "vaikams"
   scrape_and_save_data(initial_query, time_limit=60, return_format='csv' )

