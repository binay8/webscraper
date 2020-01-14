#%%
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = r"https://www.bestbuy.com/site/acer-s271hl-27-led-fhd-monitor-black/6051018.p?skuId=6051018"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
page = requests.get(url=URL, headers= headers)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="shop-product-title-a677fcee-e6ea-49d2-a61c-1f0f25946e41").get_text()
title = title.split("if ('")[0]


# price = soup.find("div", {"class": "priceView-hero-price priceView-customer-price"}).get_text()
# price = float(price[1:4])
price = 200
price_list = []
price_list.append(price)

def check_price():
    page = requests.get(url=URL, headers= headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="shop-product-title-a677fcee-e6ea-49d2-a61c-1f0f25946e41").get_text()
    title = title.split("if ('")[0]


    price = soup.find("div", {"class": "priceView-hero-price priceView-customer-price"}).get_text()
    price = float(price[1:4])

    if price != price_list[-1]:
        price_list.append(price)
        if(price < price_list[-2]):
            send_email()
            print("email sent!")
    else:
        print('No Price Update!')
        
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('binayraut8@gmail.com','hmzhcdnpcpgitmet')
    subject = "Acer Monitor Price Fell Down!"
    body = f"Acer monitor's price in Best Buy fell down. New price is {price_list[-1]}"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'binayraut8@gmail.com',
        'binay0009@hotmail.com',
        msg
    )
    print("Email sent")
    
    server.quit()

check_price()
        



# %%
