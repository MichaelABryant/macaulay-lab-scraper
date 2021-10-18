#import packages
from selenium import webdriver
import time
import pandas as pd
import numpy as np
from selenium.common.exceptions import NoSuchElementException 

#function for requesting number of albums
def get_birds(num_birds, verbose):
    
    '''Gathers albums as a dataframe, scraped from rateyourmusic.com'''   
    
    #initialize chrome driver
    driver = webdriver.Chrome(executable_path="C:/Users/malex/Desktop/cornell lab birds/chromedriver.exe")
    driver.set_window_size(1120, 1000)

    #url to begin scraping from
    url = 'https://search.macaulaylibrary.org/catalog?yr=YCUSTOM&mediaType=p&sort=rating_rank_desc&ey=2011&searchField=region&regionCode=US-CA-073&by=2011&q=San%20Diego,%20California,%20United%20States%20(US)'
    driver.get(url)
    
    #wait for browser to open
    time.sleep(10)
    
    #initialize albums array
    birds = []
    
    pics_dir = []
    
    page_clicks = round(num_birds/30)
    
    print('{}% loaded'.format(round(((1-(page_clicks/round(num_birds/30)))*100),2)))
    
    if page_clicks > 0:
        
        while True:
            
            try:
            
                driver.find_element_by_xpath('.//button[@id="show_more"]').click()
                page_clicks -= 1
                time.sleep(5)
                
                print('{}% loaded'.format(round(((1-(page_clicks/round(num_birds/30)))*100),2)))
                
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
                
                if page_clicks < 1:
                    
                    break
                
            except NoSuchElementException:
                
                break
    
    pics_dir = driver.find_elements_by_xpath('.//div[@class="ResultsGallery-background"]//a[@class="ResultsGallery-link"]')    
          
        
    for directory in pics_dir:
        
        pic_id = directory.get_attribute('data-asset-id')
    
        #xpath to specify album ranking
        xpath = './/a[@data-asset-id="'
        xpath += str(pic_id)
        xpath += '"]'
    
        #initialize variable to break while loop
        collected_successfully = False
    
        #runs until collected_successfully = True
        while not collected_successfully:
            
            #try to find items for scraping
            try:
                
                img = driver.find_element_by_xpath('{}//figure[@class="ResultsGallery-figure"]//img[@class="ResultsGallery-image show"]'.format(xpath))
                name = img.get_attribute('alt')
                url = img.get_attribute('src')
                
                #append scraped information to albums array
                birds.append({"Name" : name,
                              "URL" : url})
                
                name = np.nan
                url = np.nan
                
                #set true to break while loop
                collected_successfully = True
                
                
            
            #if page hasn't loaded yet wait 5 seconds
            except NoSuchElementException:
                print('error during collection.')
                name = np.nan
                url = np.nan
                break


        
        if len(birds) == num_birds:
            break
         
        
    #return requested albums as a dataframe
    return pd.DataFrame(birds)