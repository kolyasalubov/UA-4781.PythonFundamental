
from pyowm import OWM
from pyowm.utils.config import get_default_config
from datetime import datetime


# ---------- FREE API KEY examples ---------------------


input_language = input("Вибери солов’їну: ") 

config_dict = get_default_config()
config_dict['language'] = input_language
owm = OWM('ef2206ff5da67de63306d0b143e20872', config_dict)
mgr = owm.weather_manager()

input_city = input("where the chestnuts are bloomingг: ")
# Search for current weather in City and get details
observation = mgr.weather_at_place(input_city)
w = observation.weather

from datetime import datetime

time_now = datetime.now()
print(f"День: {time_now:%A, %d %B %Y}")
print("Час:", time_now.time())


mgr2 = owm.geocoding_manager()
city_location = mgr2.geocode(input_city)

lat = city_location[0].lat
lon = city_location[0].lon

# one_call = mgr.one_call(lat=lat, lon=lon)
# national_weather_alerts = one_call. national_weather_alerts

# for alert in national_weather_alerts:
#     print(alert.title)   

humidity = w.humidity               
temperature_max = w.temperature('celsius')['temp_max']  
temperature = w.temperature('celsius')['temp']
temperature_min = w.temperature('celsius')['temp_min']

print(f"У місті {input_city} зараз: {w.detailed_status}")
print(f"У місті {input_city} вологість повітря становить {humidity}")
print(f"У місті {input_city} температура повітря становить {temperature}")
print(f"У місті {input_city} максимальна температура повітря становить {temperature_max}")
print(f"У місті {input_city} мінімальна температура повітря становить {temperature_min}")