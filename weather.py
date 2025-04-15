import requests
from datetime import datetime

def get_weather(city, api_key, forecast=False):
    if forecast:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not forecast:
            main = data['main']
            weather = data['weather'][0]
            wind = data['wind']
            sys = data['sys']

            sunrise = datetime.utcfromtimestamp(sys['sunrise']).strftime('%H:%M:%S')
            sunset = datetime.utcfromtimestamp(sys['sunset']).strftime('%H:%M:%S')

            weather_info = (
                f"Temperature: {main['temp']}°C\n"
                f"Humidity: {main['humidity']}%\n"
                f"Weather: {weather['description'].capitalize()}\n"
                f"Wind Speed: {wind['speed']} m/s\n"
                f"Feels Like: {main['feels_like']}°C\n"
                f"Pressure: {main['pressure']} hPa\n"
                f"Sunrise: {sunrise} UTC\n"
                f"Sunset: {sunset} UTC\n"
            )
            return weather_info, f"http://openweathermap.org/img/wn/{weather['icon']}@2x.png"

        else:
            forecast_info = f"Weather forecast for the next 3 days:\n"
            
            # Get the data for the next 3 days (forecast returns every 3 hours)
            days = ['Morning (6AM)', 'Afternoon (12PM)', 'Evening (6PM)']
            day_count = 0
            for day in range(0, 3):
                forecast_info += f"\nDay {day+1}:\n"
                for time_slot in range(3):  # Morning, Afternoon, Evening
                    # Get the closest time index for each period (6AM, 12PM, 6PM)
                    index = day_count * 8 + time_slot  # OpenWeather API returns every 3 hours
                    timestamp = datetime.utcfromtimestamp(data['list'][index]['dt'])
                    temp = data['list'][index]['main']['temp']
                    description = data['list'][index]['weather'][0]['description']

                    forecast_info += f"{days[time_slot]} - Temp: {temp}°C, {description.capitalize()}\n"
                
                day_count += 1  # Move to the next day (every 8 intervals is a day)

            return forecast_info, f"http://openweathermap.org/img/wn/{data['list'][0]['weather'][0]['icon']}@2x.png"

    except requests.exceptions.HTTPError as err:
        return f"Error: {err.response.status_code} - {err.response.text}", ""
    except requests.exceptions.RequestException as err:
        return f"Error: {err}", ""
