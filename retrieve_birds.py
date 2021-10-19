import scraper as bird
import pandas as pd

#begin scraping for 2000 bird image names/urls
df = bird.get_birds(2000, 0)

#zip and output as csv
compression_opts = dict(method='zip', archive_name='bird_urls_2011.csv')  
df.to_csv('bird_urls_2011.zip', index=False, compression=compression_opts)
