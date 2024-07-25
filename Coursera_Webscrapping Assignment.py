#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[2]:


import yfinance as yf

tesla_data = yf.download("TSLA", period="max")

tesla_data.reset_index(inplace=True)

tesla_data.head()


# In[10]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='historical_data_table table')
    rows = table.find_all('tr')[1:]  # Skip the header row
    years = []
    revenues = []
    for row in rows:
        cols = row.find_all('td')
        year = cols[0].text.strip()
        revenue = cols[1].text.strip()
        revenue_cleaned = revenue.replace('$', '').replace(',', '')
        years.append(year)
        revenues.append(revenue_cleaned)
    tesla_revenue = pd.DataFrame({
        'Year': years,
        'Revenue': revenues
    })
tesla_revenue.tail()


# In[12]:


import yfinance as yf
import pandas as pd
gme_data = yf.download('GME',period='max')
gme_data.reset_index(inplace=True)
gme_data.to_csv('gme_data.csv', index=False)
gme_data.head()


# In[14]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='historical_data_table table')
    rows = table.find_all('tr')[1:]  # Skip the header row
    years = []
    revenues = []
    for row in rows:
        cols = row.find_all('td')
        year = cols[0].text.strip()
        revenue = cols[1].text.strip()
        revenue_cleaned = revenue.replace('$', '').replace(',', '')
        years.append(year)
        revenues.append(revenue_cleaned)
    gme_revenue = pd.DataFrame({
        'Year': years,
        'Revenue': revenues
    })
gme_revenue.tail()


# In[23]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, title):
    plt.figure(figsize=(14, 7))

    plt.plot(stock_data.index, stock_data['Close'], label='Stock Close Price', color='blue')

    # Plot revenue data
    plt.plot(revenue_data['Year'], revenue_data['Revenue'], label='Annual Revenue', color='orange', marker='o')

    plt.title(f'{title} Stock Price and Revenue')
    plt.xlabel('Date')
    plt.ylabel('Value')

    plt.legend()

    plt.grid(True)

    plt.show()


# In[24]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# In[25]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




