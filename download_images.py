####cleaning data

import pandas as pd
import numpy as np

bird2012 = pd.read_csv('bird_urls_2012.csv')
bird2013 = pd.read_csv('bird_urls_2013.csv')
bird2014 = pd.read_csv('bird_urls_2014.csv')
bird2015 = pd.read_csv('bird_urls_2015.csv')


frames = [bird2012, bird2013, bird2014, bird2015]

df = pd.concat(frames)

compression_opts = dict(method='zip', archive_name='birds_10k_a.csv') 
df.to_csv('birds_10k_a.zip', index=False, compression=compression_opts)

df = pd.read_csv('birds_10k_a.csv')

####cleaning names
import clean_images
    
df = clean_images.clean_bird_images(df)

####making directories and downloading images

import retrieve_images

retrieve_images.download_images(df)