
import pandas as pd
import numpy as np

#read in freshly scraped dataframes
bird2012 = pd.read_csv('bird_urls_2012.csv')
bird2013 = pd.read_csv('bird_urls_2013.csv')
bird2014 = pd.read_csv('bird_urls_2014.csv')
bird2015 = pd.read_csv('bird_urls_2015.csv')

#list of dataframes
frames = [bird2012, bird2013, bird2014, bird2015]

#concatenate dataframes
df = pd.concat(frames)

#save dataframe containing previous dataframes as zip/csv
compression_opts = dict(method='zip', archive_name='birds_10k_a.csv') 
df.to_csv('birds_10k_a.zip', index=False, compression=compression_opts)

#reload dataframe
df = pd.read_csv('birds_10k_a.csv')

####cleaning names
import clean_images

#use user-defined function to clean image names
df = clean_images.clean_bird_images(df)

####making directories and downloading images

import retrieve_images

#use user-defined function to download images from URLs
retrieve_images.download_images(df)
