'''
Created on 5 nov. 2021

@author: U219200
'''
from pysocialwatcher import watcherAPI, constants
import pandas as pd
from pysocialwatcher.utils import call_request_fb, post_process_collection, save_after_collecting_dataframe
import pandas as pd
import time
import logging
import json
import time


df = pd.read_excel("./fb keys/region_india.xls", sheet_name="Sheet1")
regs = []
for index, row in df.iterrows():
    regs.append({"key": row['key'], "name": row['name'], "country":"IN"},)

gender_dic = {"name": "FB audience",
        "geo_locations":[{"name": "regions", "values": [region]} for region in regs],
        "genders": [0, 1, 2],
        "ages_ranges": [  {"min":13, }],
        "interests": [{"or": [6003711009918], "name": "Air conditioning"}, 
                         {"or": [], "name": "no_interest"},
                         ],
        "publisher_platforms" : ['facebook', 'instagram']
        }

age_dic =  {"name": "FB audience IN",
            "geo_locations": [{"name": "regions", "values": [region]} for region in regs],
            "genders": [0],
            "ages_ranges": [{"min":65, },
                            {"min":18, "max":34},
                            {"min":35, "max":64}
                           ],
            "interests": [{"or": [6003711009918], "name": "Air conditioning"}, 
                         {"or": [], "name": "no_interest"},
                         ],
            "publisher_platforms" : ['facebook', 'instagram']
            }

education_dic = {"name": "FB audience IN",
            "geo_locations": [{"name": "regions", "values": [region]} for region in regs],
            "genders": [0],
            "ages_ranges": [{"min": 18},
                           ],
            "scholarities":[  {"name" : "1 Less than high school", "or" : [1, 13]},
                          #{"name" : "2 Some high school", "or" : [13]},
                          {"name" : "2 High school and associate degree", "or" : [2, 4, 5, 6, 10]},
                          #{"name" : "4 Professional or associate degree", "or" : [6, 10]},
                          {"name" : "3 University and higher", "or" : [3, 7, 8, 9, 11]},
                          #{"name" : "6 Masters and Doctorate degree", "or" : [9, 11]},
                          {"name" : "7 Unspecified", "or" : [12]}
                       ],
            "interests": [{"or": [6003711009918], "name": "Air conditioning"}, 
                         {"or": [], "name": "no_interest"},
                         ],
            "publisher_platforms" : ['facebook', 'instagram']
            }


json_dir = "./jsons/"
with open(json_dir+'in_states_age.json', 'w') as fp:
    json.dump(age_dic, fp)
fp.close()

if __name__ == '__main__':
    watcher = watcherAPI() 
    token = # ENTER YOUR TOKEN
    account = # ENTER YOUR ACCOUNT ID
    
    #watcher.print_interests_given_query("Family")
    watcher.add_token_and_account_number(token, account) 
    
    directory = 'C:/Users/U219200/OneDrive - IIASA/Projects/SM_AIRCO/data/fb keys/'
    
    #df = watcher.get_geo_locations_given_query_and_location_type(None, ["region"], country_code='BR')
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    
    
    
    input_file = json_dir+'in_states_age.json'
    watcher.run_data_collection(input_file)
    #collection_dataframe = pd.read_csv("dataframe_collecting_1646647833.csv")
    #post_process_collection(collection_dataframe)
    #save_after_collecting_dataframe(collection_dataframe, directory)

    

#print(df)
#df.to_excel(directory+'brazil_states.xlsx')
