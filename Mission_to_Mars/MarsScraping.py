#!/usr/bin/env python
# coding: utf-8

# Import beeded tools
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager



def scrape_mars():
    #Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Set the url parameter
    url = 'https://redplanetscience.com/'

    #Creative the browser to find the code
    browser.visit(url)


    #Create the HTML as a parameter, then use Beuatiful soup to clean it up and read it.
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Add all titles and teaser texts to dictionaries.
    titles = soup.find_all('div', class_='content_title')[0].text
    teasers = soup.find_all('div', class_='article_teaser_body')[0].text

    #Create Dictionary
    article_df = {'Titles': titles, "Teaser": teasers}
    #article_df = pd.DataFrame(data=article_df)
    #article_df




    #Scraping the JPLL Mars Sapce Images
    url = 'https://spaceimages-mars.com/'

    #Creative the browset to find the code
    browser.visit(url)

    #Create the HTML as a parameter, then use Beuatiful soup to clean it up and read it.
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    #Scrape the featuyred image url
    featured_image_url = soup.find_all('img')[1]['src']
    featured_image_url_full = 'https://spaceimages-mars.com/' + featured_image_url


    #Pulling the data from Mars facts
    #Scraping the JPLL Mars Sapce Images
    url = 'https://galaxyfacts-mars.com/'

    #Creative the browset to find the code
    mars_fact_table = pd.read_html(url)
    mars_fact_table

    #Save Mars data to table
    mars_fact_table = mars_fact_table[0]
    mars_fact_table.head()


    # In[12]:


    mars_fact_table_html = mars_fact_table.to_html(classes="table table-striped")


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
    hemisphere_page_url = []

    for hemisphere in hemisphere_links:
        #hemisphere_dict = {}
        link = hemisphere.find('a')['href']
        # full_link = 'https://marshemispheres.com/' + link
        hemisphere_page_url.append(link)
        #hemisphere_name = hemisphere.find('h3').text
        #hemisphere_list.append(hemisphere_name)
        #hemisphere_dict = {
        #    "Hemispheres" : hemisphere_name,
        #    "Image_URLs" : full_link
        #}
        #hemisphere_list.append(hemisphere_dict)
    # In[17]:


    hemisphere_toscrape_url_list = ['https://marshemispheres.com/' + url for url in hemisphere_page_url]


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
        hemisphere_dict = {}
        soup = BeautifulSoup(html, 'html.parser')
        hemisphere_name = soup.find('h2', class_='title').get_text()
        #hemisphere_list.append(hemisphere_name)
        soup_filtered = soup.find_all('div', class_='wide-image-wrapper')
        for soup in soup_filtered:
                link = soup.find('img', class_='wide-image')['src']
                #hemisphere_image_urls.append(link)
                hemisphere_fullresimage_url = 'https://marshemispheres.com/' + link
                hemisphere_dict = {
                    "Hemispheres" : hemisphere_name,
                    "Image_URLs" : hemisphere_fullresimage_url
                }
                hemisphere_list.append(hemisphere_dict)
        #image_url = soup_filtered.find('a')['src']
        #print(soup_filtered)


    # In[22]:


    #hemisphere_image_urls


    # In[23]:


    # hemisphere_fullresimage_url = ['https://marshemispheres.com/' + url for url in hemisphere_image_urls]
    #hemisphere_fullresimage_url


    # In[37]:


    #hemisphere_list


    # In[64]:


    #hemisphere_info_dict = {
    #    "Hemispheres" : hemisphere_list,
    #    "Image_URLs" : hemisphere_fullresimage_url
    #}


    # In[ ]:

    browser.quit()

    mars_scraping_data = {
        "mars_image" : featured_image_url_full,
        "latest_mars_news" : article_df,
        "mars_fact_table" : mars_fact_table_html,
        "mars_hemispheres" : hemisphere_list
    }

    return mars_scraping_data