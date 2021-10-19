import re


def clean_bird_images(df):
    
    '''Cleans the "Name" column of the bird df by removing photographers name and forward slashes'''

    Name = []
    
    #creates a list of bird names without the photographers name
    for i in df.Name:
        
        Name.append(re.findall('.*(?= -)',i)[0])
        
    #implement changes in dataframe  
    df['Name'] = Name
    
    #find names with forward slashes
    Names_slashes = df.Name[df.Name.str.contains('/')]
    
    #initialize list for names without forward slashes
    Names_without_slashes = Names_slashes.copy()
    
    #remove forward slashes
    for i in range(len(Names_slashes)):
        Names_without_slashes.iloc[i] = Names_slashes.iloc[i].replace('/', ' ')
    
    #implement changes in dataframe
    for i in range(len(Names_without_slashes)):
        df.Name[df.Name == Names_slashes.iloc[i]] = Names_without_slashes.iloc[i]
    
    #return the cleaned dataframe
    return df
