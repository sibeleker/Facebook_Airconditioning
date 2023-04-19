'''
Created on 22 aug. 2021

@author: U219200
'''
from pysocialwatcher import watcherAPI, constants 
from pysocialwatcher.utils import call_request_fb
import pandas as pd
import time
import logging
import json
import time


if __name__ == '__main__':
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    
    watcher = watcherAPI() 
    token = # enter your token
    account = # your account id

    watcher.add_token_and_account_number(token, account) 
    
    json_dir = "./jsons/"
    input_file = json_dir+'mex_age.json'
    watcher.run_data_collection(input_file)