import scraper as bird
import pandas as pd

df = bird.get_birds(2000, 0)

compression_opts = dict(method='zip', archive_name='bird_urls_2011.csv')  
df.to_csv('bird_urls_2011.zip', index=False, compression=compression_opts)