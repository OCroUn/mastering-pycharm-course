import requests
import json
import sqlalchemy

resp = requests.get('https://weather.talkpython.fm/api/weather?city=portland&state=OR&country=US&units=imperial')
resp.raise_for_status()

data = resp.json()
temp = data['forecast']['temp']


print(f"Hello world, it's {temp} outside!")

