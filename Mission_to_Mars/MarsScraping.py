#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


#Setup Splinter

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


#Set the url parameter
url = 'https://redplanetscience.com/'


# In[4]:


#Creative the browset to find the code
browser.visit(url)


# In[5]:


#Create the HTML as a parameter, then use Beuatiful soup to clean it up and read it.
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#Add all titles and teaser texts to dictionaries.
title = soup.find_all('div', class_='content_title')
teaser = soup.find_all('div', class_='article_teaser_body')


# In[6]:


#Transform the dictionaries into a dataframe
article_df = {'Titles': title, "Teaser": teaser}
article_df = pd.DataFrame(data=article_df)


# In[7]:


#Identify the first title and teaser
first_title = article_df.iloc[0, 0]
first_teaser = article_df.iloc[0, 1]
print(first_title)
print(first_teaser)


# In[8]:


#Scraping the JPLL Mars Sapce Images
url = 'https://spaceimages-mars.com/'

#Creative the browset to find the code
browser.visit(url)

#Create the HTML as a parameter, then use Beuatiful soup to clean it up and read it.
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[9]:


#Scrape the featuyred image url
featured_image_url = soup.find_all('img')[1]['src']
featured_image_url


# In[10]:


#Pulling the data from Mars facts
#Scraping the JPLL Mars Sapce Images
url = 'https://galaxyfacts-mars.com/'

#Creative the browset to find the code
mars_fact_table = pd.read_html(url)
mars_fact_table


# In[11]:


#Save Mars data to table
mars_fact_table = mars_fact_table[1]
mars_fact_table.head()


# In[12]:


mars_fact_table_html = mars_fact_table.to_html()


# In[13]:


mars_fact_table_html.replace('\n', '')


# In[14]:


#Setup beautful soup for scraping hemisphere data
#Pulling the data from Mars facts
#Scraping the JPLL Mars Sapce Images
url = 'https://marshemispheres.com/'

#Creative the browset to find the code
browser.visit(url)

#Create the HTML as a parameter, then use Beuatiful soup to clean it up and read it.
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[15]:


hemisphere_links = soup.find_all('div', class_='item')


# In[16]:


hemisphere_list = []
hemisphere_url = []

for hemisphere in hemisphere_links:
    link = hemisphere.find('a')['href']
    hemisphere_url.append(link)
    hemisphere_name = hemisphere.find('h3')
    hemisphere_list.append(hemisphere_name)


# In[17]:


hemisphere_toscrape_url_list = ['https://marshemispheres.com/' + url for url in hemisphere_url]


# In[18]:


hemisphere_toscrape_url_list


# In[19]:


#hemisphere_df = {'Hemisphere': hemisphere_list, "link":hemisphere_toscrape_url_list }
#hemisphere_df = pd.DataFrame(data=hemisphere_df)
#hemisphere_df


# In[20]:


hemisphere_names = []
hemisphere_image_urls = []


# In[21]:


#Setup beautful soup for scraping hemisphere data
#Pulling the data from Mars facts
#Scraping the JPLL Mars Sapce Images
url = 'https://marshemispheres.com/cerberus.html'

#Creative the browset to find the code
browser.visit(url)

#Create the HTML as a parameter, then use Beuatiful soup to clean it up and read it.
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

for url in hemisphere_toscrape_url_list:
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup_filtered = soup.find_all('div', class_='description')
    for soup in soup_filtered:
            link = soup.find('a')['href']
            hemisphere_image_urls.append(link)
    #image_url = soup_filtered.find('a')['src']
    #print(soup_filtered)


# In[22]:


hemisphere_image_urls


# In[23]:


hemisphere_fullresimage_url = ['https://marshemispheres.com/' + url for url in hemisphere_image_urls]
hemisphere_fullresimage_url


# In[37]:


hemisphere_list


# In[64]:


hemisphere_image_urls_df = [hemisphere_list, hemisphere_fullresimage_url]
hemisphere_image_urls_df = pd.DataFrame({'Hemisphere': hemisphere_list,
                                        'img_url' : hemisphere_fullresimage_url})


# In[65]:


hemisphere_image_urls_df


# In[66]:


hemisphere_image_urls_df


# In[67]:


hemisphere_image_urls_dict = hemisphere_image_urls_df.to_dict()


# In[68]:


hemisphere_image_urls_dict


# In[ ]:





# In[ ]:




