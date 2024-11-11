import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price
    html = requests.get(product_laughs).content
    soup = BeautifulSoup(html,'html.parser')
    
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    price_laughs = soup.find("span",{"class":"regular-price"}).get_text()
    product_name_laughs = soup.find("div",{"class":"product-name"}).get_text()


    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    html = requests.post(product_glomark).content
    soup = BeautifulSoup(html,'html.parser')
    pro = soup.find('script',type='application/ld+json').get_text()
    pro = json.loads(pro)
    price_glomark = pro['offers'][0]['price']
    product_name_glomark = pro['name']
    price_laughs = price_laughs.replace('Rs.','')
    
    #TODO: Parse the values as floats, and print them.
    price_laughs = float(price_laughs)
    price_glomark = float(price_glomark)

    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')