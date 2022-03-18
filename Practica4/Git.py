import requests
from pprint import pprint
username = str(input("Ingresa un nombre de usuario de Github: "))
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint(user_data)