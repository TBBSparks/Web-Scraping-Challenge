#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import re
import pandas as pd
import time
import lxml

def init_browser():
    executable_path = {"executable_path" : "geckodriver"}
    return Browser("firefox", **executable_path, headless=False)

mars_web = {}

def scrape_news():
    
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    time.sleep(10) # Sleep for 10 seconds
    soup = bs(html, "html.parser")
    #latest_news_date = (soup.find_all('div', class_="list_date"))[0].get_text()
    latest_news_title = soup.find("div", class_="content_title").text
    latest_news_paragraph = soup.find("div", class_="article_teaser_body").text
    
    #mars_web['latest_news_date'] = latest_news_date
    mars_web["latest_news_title"] = latest_news_title
    mars_web["latest_news_paragraph"] = latest_news_paragraph
   
    browser.quit()
    return mars_web
    
def scrape_marsImage():
    
    browser = init_browser()
    
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(5) # Sleep for 5 seconds
    html=browser.html
    soup = bs(html, 'html.parser')
    
    image = (soup.find_all('div', class_='carousel_items')[0].a.get('data-fancybox-href'))
    
    featured = 'https://www.jpl.nasa.gov'+ image
    
    mars_web['featured_image'] = featured
    
    browser.quit()
    return mars_web
    
def scrape_marsTwitter():

    browser = init_browser()

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(5) # Sleep for 5 seconds
    html=browser.html
    soup = bs(html, 'html.parser')
    
    #mars_weather = (soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].get_text())
    mars_weather = soup.find_all('div', class_='js-tweet-text-container')
    mars_web['mars_weather'] = mars_weather
    
    browser.quit()      
    return mars_web
    
def scrape_marsFacts():
    browser = init_browser()
    
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    time.sleep(5) # Sleep for 5 seconds
    html=browser.html
    soup = bs(html, 'html.parser')
    tables_df = ((pd.read_html(url))[0]).rename(columns={0: "Attribute", 1: "Value"}).set_index(['Attribute'])
    html_table = (tables_df.to_html()).replace('\n', '')
    
    mars_web['mars_data'] = html_table
    browser.quit()
    return mars_web
        
def scrape_marsH1Cerberus():

    browser = init_browser()

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    time.sleep(5) # Sleep for 5 seconds
    html=browser.html
    soup = bs(html, 'html.parser')
    cerberus_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    mars_web['cerberus_url'] = cerberus_url
    
    browser.quit()
    return mars_web
    
def scrape_marsH2Schiaparelli():
 
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    time.sleep(5) # Sleep for 5 seconds
    html=browser.html
    soup = bs(html, 'html.parser')
    schiaparelli_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    mars_web['schiaparelli_url'] = schiaparelli_url

    browser.quit()
    return mars_web
    
def scrape_marsH3SyrtisMajor():        

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    time.sleep(5) # Sleep for 5 seconds
    html=browser.html
    soup = bs(html, 'html.parser')
    syrtis_major_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    mars_web['syrtis_major_url'] = syrtis_major_url

    browser.quit()
    return mars_web
        
def scrape_marsH4VallesMarineris():     

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    time.sleep(5) # Sleep for 5 seconds
    html=browser.html
    soup = bs(html, 'html.parser')
    valles_marineries_url= (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    mars_web['valles_marineries_url'] = valles_marineries_url

    browser.quit()
    return mars_web