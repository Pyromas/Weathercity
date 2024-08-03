import requests
import pytz
from timezonefinder import TimezoneFinder
from datetime import datetime


def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    return response.json()


def get_local_time(lat, lon):
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=lat, lng=lon)
    timezone = pytz.timezone(timezone_str)
    local_time = datetime.now(timezone)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

# city_name = 'CityName'
# api_key = 'YourOpenWeatherMapAPIKey'
# weather_info = get_weather(city_name, api_key)
# local_time = get_local_time(lat, lon)
# print(f"Weather: {weather_info}")
# print(f"Local Time: {local_time}")
