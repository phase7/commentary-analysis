import requests

import json

for j in range(12):
    
    apistring = 'http://site.web.api.espn.com/apis/site/v2/sports/cricket/18815/playbyplay?contentorigin=espn&event=1153635&page=' + str(j) + '&period=1&section=cricinfo'
    r = requests.get(apistring)
    data = json.loads(r.text)
    print (json.dumps(data, indent = 2))
    input()

    # for i in range(25):
    #     if ( ('text' not in data['commentary']['items'][i] ) or ('shortText' not in data['commentary']['items'][i]) ):
    #         continue #For "NO BALL"s, there may not be any commentary, which throws "keyError"
    #     print ( data['commentary']['items'][i]['shortText'], " : ", data['commentary']['items'][i]['text'] )
    # print ('\n\n')