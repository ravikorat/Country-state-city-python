import os
import requests
import json
from settings import BASE_URL,API_HEADER,DIRECTORY,CACHE_DIR,COUNTRY_NEW_JSON
from countries import getCountry
from states import getStates
from cities import getCities



def myFunction():

    print("1. Get all countries name ")
    print("2. Get states by countries ")
    print("3. Get cities by states ")
    n= int(input("Enter your choise between 1 to 3: "))

    if n == 1:
        getCountry()

    elif n == 2: 
        getCountry() 
        country_name =input("Enter country name:").lower()
        if country_name in [country["country_name"].lower() for country in json.load(open(COUNTRY_NEW_JSON,'r'))]:
            getStates(country_name)    
        else:
            print("Country name is invalid")
    elif n == 3:
        getCountry()
        country_name =input("Enter country name :").lower()
        if country_name in [country["country_name"].lower() for country in json.load(open(COUNTRY_NEW_JSON,'r'))]:
            getStates(country_name)
        else:
            print("Country name not vaid")
        state_name=input("Enter State name :").lower()
        for country in json.load(open(COUNTRY_NEW_JSON,'r')):
            if country['country_name'].lower()==country_name:
                for state in country["states"]:
                    if state['state_name'].lower()==state_name:
                        getCities(country_name,state_name)
#     headers={
#     "Accept": "application/json",
#     "api-token": "gRJa6UbUVytRLfkoNXL9ziRj3QvKpyHDd1Rg07ARr8r7nEcFpi_eTGSxGrnJ5razRXE",
#     "user-email": "hetal@gmail.com"
#   }
#     data=requests.get("https://www.universal-tutorial.com/api/getaccesstoken",headers=headers)
#     print(data.json())


myFunction()