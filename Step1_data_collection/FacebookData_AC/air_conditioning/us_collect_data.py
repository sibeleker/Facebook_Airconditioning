'''
Created on Jul 17, 2019

@author: eker
'''
from pysocialwatcher import watcherAPI, constants 
from pysocialwatcher.utils import call_request_fb
import pandas as pd
import time
import logging
import json
import time
json_dir = "./jsons/"
directory = "./fb keys/"
df_us = pd.read_excel(directory+"US_regions.xls")
us_states = []
for index, row in df_us.iterrows():

    us_states.append({"key": row['key'], "name": row['Abbreviation'], "country":"US"},)

gender_dic =  {"name": "FB audience US",
            "geo_locations": [{"name": "regions", "values": [region]} for region in us_states], #[{"name": "countries", "values": ["RU"]}],
            "genders": [0, 1,2],
            "ages_ranges": [{"min": 18},
                           ],
            "interests": [{"or": [6003711009918], "name": "Air conditioning"}, 
                         {"or": [], "name": "no_interest"},
                         ],
            "publisher_platforms" : ['facebook', 'instagram']
            }


age_dic =  {"name": "FB audience US",
            "geo_locations": [{"name": "regions", "values": [region]} for region in us_states],#[{"name": "regions", "values": [region]} for region in italy_regions],
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

education_dic = {"name": "FB audience US",
            "geo_locations": [{"name": "regions", "values": [region]} for region in us_states],
            "genders": [0],
            "ages_ranges": [{"min": 18},
                           ],
            "scholarities":[  {"name" : "1 High school student", "or" : [1]},
                          {"name" : "2 Some high school", "or" : [13]},
                          {"name" : "3 High school grad or studying or some college", "or" : [2, 4, 5]},
                          {"name" : "4 Professional or associate degree", "or" : [6, 10]},
                          {"name" : "5 College grad or studying higher", "or" : [3, 7, 8]},
                          {"name" : "6 Masters and Doctorate degree", "or" : [9, 11]},
                          {"name" : "7 Unspecified", "or" : [12]}
                       ],
            "interests": [{"or": [6003711009918], "name": "Air conditioning"}, 
                         {"or": [], "name": "no_interest"},
                         ],
            "publisher_platforms" : ['facebook', 'instagram']
            }
income_dic = {"name": "FB audience US",
            "geo_locations": [{"name": "regions", "values": [region]} for region in us_states],#[{"name": "regions", "values": [region]} for region in italy_regions],
            "genders": [0],
            "ages_ranges": [{"min": 18},
                           ], 
            "income" : [{"name" : "Household income: top 25%-50% of ZIP codes (US)", "or": [6107813554583]}, 
                        {"name" : "Household income: top 10%-25% of ZIP codes (US)", "or": [6107813553183]}, 
                        {"name" : "Household income: top 10% of ZIP codes (US)", "or": [6107813551783]}, 
                        {"name" : "Household income: top 5% of ZIP codes (US)", "or": [6107813079183]}],
            "interests": [{"or": [6003711009918], "name": "Air conditioning"}, 
                         {"or": [], "name": "no_interest"},
                         ],
            "publisher_platforms" : ['facebook', 'instagram']
            }
relationship_dic = {"name": "FB audience US",
            "geo_locations": [{"name": "regions", "values": [region]} for region in us_states],#[{"name": "regions", "values": [region]} for region in italy_regions],
            "genders": [0],
            "ages_ranges": [{"min": 18},
                           ], 
            "relationship_statuses": [{"name" : "married or living together", "or" : [3, 7, 8]},
                                     {"name" : "all others relationship", "or" : [1, 2, 4, 6, 9, 10, 11, 12, 13]}] ,
            "interests": [{"or": [6003711009918], "name": "Air conditioning"}, 
                         {"or": [], "name": "no_interest"},
                         ],
            "publisher_platforms" : ['facebook', 'instagram']
            }
family_dic = {"name": "FB audience US",
            "geo_locations": [{"name": "regions", "values": [region]} for region in us_states],#[{"name": "regions", "values": [region]} for region in italy_regions],
            "genders": [0],
            "ages_ranges": [{"min": 18},
                           ], 
            "family_statuses" : [{"name" : "parents of 0-8 yrs old", "or" : [6023005372383, 6023005458383, 6023005529383, 6023005570783]},
                             {"name" : "parents of 9-18 yrs old", "or" : [6023080302983, 6023005681983]},
                             {"name" : "all family", "or" : []}],
            "interests": [{"or": [6003711009918], "name": "Air conditioning"}, 
                         {"or": [], "name": "no_interest"},
                         ],
            "publisher_platforms" : ['facebook', 'instagram']
            }

attribute_dic = {'gender' : gender_dic,
                 'age' : age_dic, 
                 'education' : education_dic, 
                 'income' : income_dic, 
                 'family' : family_dic, 
                 'relationship' : relationship_dic}


if __name__ == '__main__':
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    

    watcher = watcherAPI()   
    token = # your token
    account = # your account id

    watcher.add_token_and_account_number(token, account)  
    watcher.check_tokens_account_valid()

    for attribute, dic in attribute_dic.items():
        if attribute in ['education']:
            input_file = json_dir+'us_{}.json'.format(attribute)
            with open(input_file, 'w') as fp:
                json.dump(dic, fp)
            watcher.run_data_collection(input_file)

