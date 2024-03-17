
def getWeather(city):
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text = result)
    