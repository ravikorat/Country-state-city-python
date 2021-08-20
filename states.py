import os
import json
import requests
from settings import BASE_URL,API_HEADER,COUNTRY_NEW_JSON
from countries import getCountry

def getStates(country_name):
    getCountry()
    # import pdb; pdb.set_trace()
    with open(COUNTRY_NEW_JSON,'r+') as country_file:
        data=json.load(country_file)
        for country in data:
            if country['country_name'].lower() == country_name:
                if 'states' in country.keys():
                    try:
                        country['states']==''
                    except :
                        state_response = requests.get(BASE_URL+'/api/states/'+country_name,headers=API_HEADER)
                        if state_response.ok:
                            country['states'] = state_response.json()
                        else:
                            return(state_response,state_response.json())                   
                else:
                    state_response = requests.get(BASE_URL+'/api/states/'+country_name,headers=API_HEADER)
                    # import pdb; pdb.set_trace()
                    if state_response.ok:
                        country['states'] = state_response.json()
                        
                    else:
                        return(state_response,state_response.json())
                
                country_file.seek(0)
                json.dump(data,country_file,indent=4)
        
    
