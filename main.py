import requests
import json
from sys import argv

param = argv[1]
api_get = requests.get('https://api.domainsdb.info/v1/domains/search?' , params={'domain' : param})
api_answer = api_get.json()
print(api_answer['domains'][0]['NS'])
