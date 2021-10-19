import os

import urllib.request


def download_images(df):
    
    '''Downloads images from dataframe containing bird names and image urls'''

    directories = df.Name.unique()
    
    parent_dir = 'C:/Users/malex/Desktop/cornell lab birds/images/'
    
    for directory in directories:
        
        print(directory)
        
        os.chdir(parent_dir)
        
        path = os.path.join(parent_dir, directory)
        
        try: 
            
            # mode
            mode = 0o666
            
            os.mkdir(path, mode)
            
            
        except:
            
            os.chdir(path)
        
        os.chdir(path)
        
        for i in range(len(df[df.Name == directory])):
                              
            # setting filename and image URL
            filename = '{}_a.jpg'.format(i)
            image_url = df.URL[df.Name == directory].iloc[i]
    
            # calling urlretrieve function to get resource
            urllib.request.urlretrieve(image_url, filename)
