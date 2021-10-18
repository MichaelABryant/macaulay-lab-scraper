import re


def clean_bird_images(df):

    Name = []
    
    for i in df.Name:
        
        Name.append(re.findall('.*(?= -)',i)[0])
        
        
    df['Name'] = Name
    
    Names_slashes = df.Name[df.Name.str.contains('/')]
    
    Names_without_slashes = Names_slashes.copy()
    
    for i in range(len(Names_slashes)):
        Names_without_slashes.iloc[i] = Names_slashes.iloc[i].replace('/', ' ')
    
    
    for i in range(len(Names_without_slashes)):
        df.Name[df.Name == Names_slashes.iloc[i]] = Names_without_slashes.iloc[i]
        
    return df
