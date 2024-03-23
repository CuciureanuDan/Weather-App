
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder 
from datetime import datetime
import pytz
import requests


def getWeather(city, clock_widget, timezone_widget):
    
    geolocator = Nominatim(user_agent="getINFO")
    location = geolocator.geocode(city)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone_widget.config(text = result)
    
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")

    clock_widget.config(text=current_time)

    lat =str( location.latitude)
    lon = str(location.longitude)

    #api= "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={db8271986daa8d8578383752c3ae182e}"
    api = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, "db8271986daa8d8578383752c3ae182e")



    json_data = requests.get(api).json()


    #current 

    temp = round( json_data['main']['temp'] - 273.15 ,1) # transforming in celsius and round it to one decimal
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    description = json_data['weather'][0]['description']

    print(temp)
    print(humidity)
    print(wind)
    print(description)


    