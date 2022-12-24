#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import datetime
import time

import smtplib


# In[5]:


url = "https://www.amazon.com/SAMSUNG-Premiere-Projector-Built-SP-LSP7TFAXZA/dp/B08DL6KY3Z?ref_=Oct_DLandingS_D_ecce27f0_78&th=1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

webpage = requests.get(url, headers=headers)    
    
soup1 = BeautifulSoup(webpage.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")


# In[13]:


title = soup2.find(id="productTitle").get_text().strip()
price = soup2.find("span", class_="a-price-whole").get_text()


# In[28]:


price = price.replace("\n","").replace(".", "").strip()


# In[30]:


today = datetime.date.today()
print(today)


# In[29]:


import csv

header = ["Title", "Price", "Date"]
data = {title, price, today}

with open("AmazonWebScraping.csv", "w", newline="", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[33]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Hunani Trading Co\data scrape\Amazon\AmazonWebScraping.csv")
df


# In[34]:


#appending data to csv

with open("AmazonWebScraping.csv", "a+", newline="", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('amirejaz790@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Samsung smart TV you want is below $1500! Now is your chance to buy!"
    body = "Amir, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'amirejaz790@gmail.com',
        msg
     
    )


# In[37]:


#Combine all of the above code into one function


def check_price():
    URL = 'https://www.amazon.com/SAMSUNG-Premiere-Projector-Built-SP-LSP7TFAXZA/dp/B08DL6KY3Z?ref_=Oct_DLandingS_D_ecce27f0_78&th=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    webpage = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(webpage.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")


    title = soup2.find(id="productTitle").get_text().strip()
    price = soup2.find("span", class_="a-price-whole").get_text()
    price = price.replace("\n","").replace(".", "").strip()
    
    
    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
#     if (price <= 1500):
#         send_mail()


# In[ ]:


while(True):
    check_price()
    time.sleep(86400) #for one day


# In[ ]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Hunani Trading Co\data scrape\Amazon\AmazonWebScraping.csv")
print(df)


# In[ ]:




