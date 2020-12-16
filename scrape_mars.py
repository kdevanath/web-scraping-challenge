#!/usr/bin/env /Users/penndata/anaconda3/envs/PythonData
# coding: utf-8

import time
import os
import re
from splinter import Browser
import requests
import pandas as pd


from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    base_url = 'https://www.jpl.nasa.gov'
    mars_dict = {}


    # Create a Beautiful Soup object
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    time.sleep(1)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    #news_response  = requests.get('https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest')
    news_titles = news_soup.find('div', class_='list_text')
    news_title = news_titles.find('a')
    #news_titles = news_soup.find_all('div', class_='content_title')
    news_p = news_soup.find('div', class_='article_teaser_body')


    mars_dict['news_title'] = news_title.text
    mars_dict['news_body'] = news_p.text
    print(mars_dict)
    print()

    #Find Featured image url

    image_url = '/spaceimages/?search=&category=Mars'
    url = f'{base_url}{image_url}'
    print(url)
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    # Retrieve page with the requests module
    #response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    image_soup = BeautifulSoup(html, 'html.parser')

    #scrape for featured image 
    results = image_soup.find('article', class_="carousel_item")
    image_url = re.findall(r"'(.*?)'", results.attrs['style'])
    featured_image_url = f'{base_url}{image_url[0]}'
    mars_dict['featured_image_url'] = featured_image_url
    #print(featured_image_url)
  
    #Use pandas to get the mars facts, convert to a dictionary
    mars_facts_url = 'https://space-facts.com/mars/'
    mft = pd.read_html(mars_facts_url)
    mars_table = mft[0].set_index(0)[1].to_dict()
    #print(mars_table)
    # In[35]:
    #store this in mars_dict to render
    mars_dict['mars_facts'] = mars_table

    #Retrieve all the 4 hemispheres, get the partial html
    hemisphere_list = []
    base_url = 'https://astrogeology.usgs.gov'
    hemis_urls = f"{base_url}/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemis_response = requests.get(hemis_urls)
    hemis_soup = BeautifulSoup(hemis_response.text, 'html.parser')
    refs = hemis_soup.find_all('a',class_ = 'itemLink') #find_all('h3')
    hemisphere_image_dict = {}
    for ref in refs:
    #   print(ref)
        title = ref.find('h3')
        hemisphere_image_dict['title'] = title.text
        image_url = ref.get('href')
        url = base_url+image_url
        #print(url)
        #visit the url and scrape the reference to full image
        browser.visit(base_url+image_url)
        time.sleep(1)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        wrapper = soup.find('div',class_ = 'downloads')
        img_url = wrapper.find('a')['href']
        #print(img_url)
        hemisphere_image_dict['img_url']= img_url
        hemisphere_list.append(hemisphere_image_dict.copy())
        #print(title, img_url)

    #add this to dictionary
    mars_dict['hemispheres'] = hemisphere_list.copy()
    #for h in mars_dict['hemispheres']:
        #print(h)
    
    print(mars_dict)
    browser.quit()
    return mars_dict




