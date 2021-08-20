import os
import json
import requests
from settings import BASE_URL,API_HEADER,COUNTRY_NEW_JSON
from countries import getCountry
from states import getStates


def getCities(country_name,state_name):
    getStates(country_name)
    with open(COUNTRY_NEW_JSON,'r+') as country_file:
        data = json.load(country_file)
        for country in data:
            if country['country_name'].lower()==country_name:
                for state in country["states"]:
                    if state['state_name'].lower()==state_name:
                        if 'cities' in state.keys():
                            try:
                                state[cities] == ''
                            except :
                                cities_response=requests.get(BASE_URL+'/api/cities/'+state_name,headers=API_HEADER) 
                                if cities_response.ok:
                                    state['cities']=cities_response.json()
                                else:
                                    return(cities_response,cities_response.json())  
                        else:
                            cities_response=requests.get(BASE_URL+'/api/cities/'+state_name,headers=API_HEADER) 
                            if cities_response.ok:
                                state['cities']=cities_response.json()
                            else:
                                return(cities_response,cities_response.json()) 
                        country_file.seek(0)
                        json.dump(data,country_file,indent=4)  
                        # return(state['cities'])
        
