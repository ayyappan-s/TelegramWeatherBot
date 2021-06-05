from pyowm import OWM
import requests

owm = OWM("Openweathermap-Api")


def getForecasts(lat, lon):
    results = []
    coord_API_endpoint = "http://api.openweathermap.org/data/2.5/weather?"
    lat_long = "lat=" + str(lat) + "&lon=" + str(lon)
    join_key = "&appid=" + "Openweathermap-Api"
    units = "&units=metric"
    current_coord_weather_url = coord_API_endpoint + lat_long + join_key + units
    print(current_coord_weather_url)
    weather_data = requests.get(current_coord_weather_url).json()
    print(weather_data)

    status = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    min_temp = weather_data['main']['temp_min']
    max_temp = weather_data['main']['temp_max']
    feels_like = weather_data['main']['feels_like']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    latitude = weather_data['coord']['lat']
    longitude = weather_data['coord']['lon']
    results.append("""
        Status : {} 
        Description : {}
        Temperature : {}
        Min Temperature : {}
        Max Temperature : {}
        Feels Like : {}
        Pressure : {}
        Humidity : {}
        Wind Speed : {}
        Latitude : {}
        Longitude : {}
        """.format(status, description, temp, min_temp, max_temp, feels_like, pressure, humidity, wind_speed, latitude,
                   longitude))

    return "".join(results[:10])
