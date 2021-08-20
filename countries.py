import os
import json
import requests
from settings import BASE_URL,API_HEADER,COUNTRY_NEW_JSON,CACHE_DIR

def getCountry():
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)
    if not os.path.exists(COUNTRY_NEW_JSON):
        countries=requests.get(BASE_URL+'/api/countries/',headers=API_HEADER).json()
        with open(COUNTRY_NEW_JSON, 'w') as countries_file:
            json.dump(countries,countries_file,indent=4)   
    else:
        with open(COUNTRY_NEW_JSON, 'r') as countries_file:
            try:
                COUNTRY_NEW_JSON==''
                data=json.load(countries_file)
            except:  
                os.remove(COUNTRY_NEW_JSON)
                getCountry()
                response = requests.get(BASE_URL+'/api/countries/', headers=API_HEADER)
                if response.ok:
                    with open(COUNTRY_NEW_JSON, 'w') as region_file:
                        json.dump(response.json(), region_file, indent=4)   
                else:
                    print(response, response.json())
            
                        
            
            
    