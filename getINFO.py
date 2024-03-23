from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder 
from datetime import datetime
import pytz
import requests
import re

def checkText(text):
    """
    Check if the input text is valid.

    Args:
    text (str): The input text to be checked.

    Returns:
    bool: True if the text is valid, False otherwise.
    """
    if len(text) < 2 or not re.match(r'^[a-zA-Z\s]+$', text):
        return False
    return True


def getWeather(city, clock_widget, timezone_widget,weather_labels):    
    """
    Get weather information for a given city and update the GUI widgets.

    Args:
    city (str): Name of the city.
    clock_widget (Widget): Clock widget to be updated.
    timezone_widget (Widget): Timezone widget to be updated.
    weather_labels (list): List of weather labels to be updated.
    """

    if checkText(city):
        geolocator = Nominatim(user_agent="getINFO")
        try:
            location = geolocator.geocode(city)
        except Exception as e:
            weather_labels[0].config(text=f"Error in getting the location: {e}")
            for idx in range(1,5):
                weather_labels[idx].config(text='')
            clock_widget.config(text='')
            timezone_widget.config(text ='')
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        timezone_widget.config(text = result)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")

        clock_widget.config(text=current_time)

        lat =str( location.latitude)
        lon = str(location.longitude)

        api = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, "db8271986daa8d8578383752c3ae182e")
        json_data = requests.get(api).json()

        #current info about weather

        temp = round( json_data['main']['temp'] - 273.15 ,1) # transforming in celsius and round it to one decimal
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        description = json_data['weather'][0]['description']

        # Update weather labels
        weather_labels[0].config(text=f"The weather is for city: {city}.")
        weather_labels[1].config(text=f"Temperature: {temp}°C")
        weather_labels[2].config(text=f"Humidity: {humidity}%")
        weather_labels[3].config(text=f"Wind Speed: {wind} m/s")
        weather_labels[4].config(text=f"Description: {description}")

        for label in weather_labels:
            label.place()
    else:
        weather_labels[0].config(text=f"Wrong city name.")
        for idx in range(1,5):
            weather_labels[idx].config(text='')
        clock_widget.config(text='')
        timezone_widget.config(text ='')


    