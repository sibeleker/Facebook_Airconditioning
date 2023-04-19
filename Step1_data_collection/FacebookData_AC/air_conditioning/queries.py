'''
Created on Mar 14, 2021

@author: eker
'''

from pysocialwatcher import watcherAPI, constants
import pandas as pd

print(constants.GRAPH_SEARCH_URL)

watcher = watcherAPI() 
token = # ENTER YOUR TOKEN !!!
account = # ENTER YOUR ACCOUNT ID !!!

#watcher.print_interests_given_query("Family")
watcher.add_token_and_account_number(token, account) 

directory = './SM_AIRCO/'

#df = watcher.get_search_targeting_from_query_dataframe("Alefata")
#df = watcher.get_search_targeting_from_query_dataframe("work_positions")
#df = watcher.get_graphapisearch_dataframe("publisher_platforms")
#df = watcher.get_geo_locations_given_query_and_location_type(None, ["region"], country_code='US')


#towns = pd.read_excel(directory+'data/IN_UP_admin.xlsx', sheet_name='for fb')

towns_list = ['Peppeganj', 'Pukhrayan', 'Rasulabad', 'Sahjanwa', 'Samthar']


#print(towns.head())
dfs = []
#for index, row in towns.iterrows():
for name in towns_list:
    #name = row['name']
    print(name)
    df = watcher.get_geo_locations_given_query_and_location_type(name, ["city"], region_id="1754", country_code='IN')
    print(df)
    dfs.append(df)
df = pd.concat(dfs)


#df = watcher.get_geo_locations_given_query_and_location_type(None, ["city"], region_id="1754", country_code='IN') #UP
#df = watcher.get_interests_given_query("air conditioning")

print(df)
df.to_excel(directory+'UP_city_keys_altspelling.xlsx')


