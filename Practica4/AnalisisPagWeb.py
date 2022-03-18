import json
import requests
clav=str(input("Ingresa tu API key: "))
api_url = 'https://www.virustotal.com/vtapi/v2/url/scan'
params = dict(apikey=clav, url=(input("Ingresa la url: ")))
response = requests.post(api_url, data=params)
if response.status_code == 200:
  result=response.json()
  print(json.dumps(result, sort_keys=False, indent=4))