import pandas as pd


data= pd.read_csv('international-migration-March-2021-citizenship-by-visa-by-country-of-last-permanent-residence.csv', dtype={'year_month':str} )
                   

data_limpia= data.status[301773:401774]

print(data_limpia)

data_limpia.to_csv('international-migration-dataLimpia.csv')



