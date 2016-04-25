import requests
import json

r = requests.get('https://api.forecast.io/forecast/61707aa3bf5d6b50275f912d1e8d6888/40.1651814,-105.8572453')
parsed_json = r.json()

print parsed_json["timezone"]
print parsed_json["currently"]


