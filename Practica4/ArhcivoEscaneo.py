import json
import requests
clav=str(input("Ingresa tu API key: "))
ruta=str(input("Ingresa la ruta de tu archivo a escanear (no mayor a 32Mb) : "))

api_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = dict(apikey=clav)
with open(ruta, 'rb') as file:
  files = dict(file=(ruta, file))
  response = requests.post(api_url, files=files, params=params)
if response.status_code == 200:
  result=response.json()
  print(json.dumps(result, sort_keys=False, indent=4))