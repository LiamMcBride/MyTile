import requests
import json

api_key = "?key=d98410f070754f77a40205826222603"

base_url = "http://api.weatherapi.com/v1"

request_type = "forecast.json"

zip_code = "27519"

request_url = base_url + "/" + request_type + api_key + "&q=" + zip_code + "&days=7"

response = requests.get(request_url)
parsed = json.loads(response)

print(json.dumps(parsed, indent=4, sort_keys =True))
