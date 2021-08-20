import os

BASE_URL='https://www.universal-tutorial.com'
API_HEADER = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJoZXRhbEBnbWFpbC5jb20iLCJhcGlfdG9rZW4iOiJnUkphNlViVVZ5dFJMZmtvTlhMOXppUmozUXZLcHlIRGQxUmcwN0FScjhyN25FY0ZwaV9lVEdTeEdybko1cmF6UlhFIn0sImV4cCI6MTYxNzcxMTE2Nn0.Nv3f3tW94ekMBQi1Hj4S5991GiagTWaEkXtTIvT8H3Y",
    "Accept": "application/json"
}
DIRECTORY= os.path.dirname(os.path.abspath(__file__))
CACHE_DIR= os.path.join(DIRECTORY,'Cache')
COUNTRY_NEW_JSON=os.path.join(CACHE_DIR,'getCountry.json')