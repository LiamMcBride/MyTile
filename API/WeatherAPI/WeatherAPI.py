import requests
import json

class WeatherAPI():
    def __init__(self):
        self.api_key = "?key=d98410f070754f77a40205826222603"
        self.base_url = "http://api.weatherapi.com/v1"
        self.request_type = "forecast.json"
        self.zip_code = "24060"

    def getWeatherData(self):
        request_url = self.base_url + "/" + self.request_type + self.api_key + "&q=" + self.zip_code + "&days=1"
        return requests.get(request_url).json()

api = WeatherAPI()

print(api.getWeatherData())