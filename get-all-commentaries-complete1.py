#!/usr/bin/env python
# coding: utf-8

# ## Create api

# In[1]:


import requests
import json
import os
import io
base_dir = os.getcwd()
db_folder_name = "commentaries1"
# if os.getcwd() != base_dir:
#     os.chdir(base_dir)
with io.open("match_ids.json", "r") as file:
    matches = json.load(file)
innings_total = [1,2]



for match_id in matches:
    os.chdir(os.path.join(base_dir, db_folder_name))
    match_dir_name = str(match_id)
    
    if not os.path.exists(match_dir_name):
            os.mkdir(match_dir_name)
            
    os.chdir(match_dir_name) 
    
    for innings in innings_total:
        innings_dir_name = "innings0"+str(innings)
        
        if not os.path.exists(innings_dir_name):
            os.mkdir(innings_dir_name)
            
        os.chdir(innings_dir_name)
        j=1 #start/restart with a non-zero number
        
        while(j):
            apistr = 'http://site.web.api.espn.com/apis/site/v2/sports/cricket/5/playbyplay?contentorigin=espn&event='+ str(match_id) +'&page=' + str(j) + '&period='+str(innings)+'&section=cricinfo'
            r = requests.get(apistr)
            data = r.json()
            items = data["commentary"]["items"]
            
            if  len(items) == 0:
                j = 0
                os.chdir("..")
                continue
                
            #my work goes here--------------------------
            with io.open("comm_part"+str(j)+".json", "w") as file:
                json.dump(data,file)

            j += 1

