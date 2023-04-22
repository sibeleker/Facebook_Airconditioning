# Facebook_Airconditioning
This repository hosts the code and data used for analyzing the social heterogeneity of air-conditioning interest based on Facebook and Instagram audience size data. The procedure and results are published in [Eker et al. (2023)](https://www.cell.com/one-earth/fulltext/S2590-3322(23)00145-8). Below is a short description of the procedure and how the code presented in this repository was used in the analysis. 

Citation : 
Eker S, Mastrucci A, Pachauri S, van Ruijven B. (2023) Social media data shed light on air-conditioning interest of heat-vulnerable regions and sociodemographic groups. One Earth 6(4) 428-440. doi: 10.1016/j.oneear.2023.03.011 

## Step 1: Data collection from Facebook Marketing API

I used [psSocialWatcher](https://github.com/maraujo/pySocialWatcher) for automated data collection from Facebook API. To be able to make custom changes in pySocialWatcher, I worked on a local pydev project that can be found in **Step1_data_collection/FacebookData_AC/**. To clean the data collection output and bring it to a more compact format suitable for my analysis, I used the **FBdata_cleaning.ipynb** 

Please note that, due to privacy reasons, I removed the token and account IDs that refer to my account on the Facebook Marketing ID. The code would not work without inputting a valid token and account ID. 

Data collection involves different geographic specifications for four countries (US, Italy, Mexico, India), and then for 136 countries. Geo-codes of states, regions, towns or countries are obtained from the Marketing API with relevant queries, which can be found in **queries.py** 

## Step 2: Comparison of survey and social media data

**Step2_Survey_analysis/** includes all data and code used in producing Figure 1 and 2 published in [Eker et al. (2023)](https://www.cell.com/one-earth/fulltext/S2590-3322(23)00145-8).

## Step 3: Analysing global online interest in air-conditioning

**penetration.ipynb** includes the code for the global penetration analysis (to what extent Facebook audience size is representative of a country's population).

**global_ac.ipynb** includes the code in analysing the global extent and heterogeneity of AC interest. In addition to this code, the data used in producing Figure 3 and 4 published in [Eker et al. (2023)](https://www.cell.com/one-earth/fulltext/S2590-3322(23)00145-8) is in the **Step3_global_analysis/** directory. 




   





