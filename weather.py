import requests
import json

API_KEY = "61707aa3bf5d6b50275f912d1e8d6888"
LAT = 40.1651814
LONG = -105.8572453

r = requests.get('https://api.forecast.io/forecast/%s/%d,%d' % (API_KEY, LAT, LONG))
parsed_json = r.json()

print parsed_json["timezone"]
print parsed_json["currently"]


