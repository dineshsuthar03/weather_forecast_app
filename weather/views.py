import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages  # Import Django messages framework
from dotenv import load_dotenv
import os
from django.utils.timezone import datetime
from django.utils import timezone

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment variables
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

def get_weather_data(city_name):
    try:
        # OpenWeatherMap API URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        # If the response is successful (HTTP status code 200)
        if response.status_code == 200:
            data = response.json()
            # Check if the city is found in the response
            if data['cod'] == 200:
                # Extract weather details
                weather_info = {
                    'city_name': data['name'],
                    'country': data['sys']['country'],
                    'temperature': data['main']['temp'],
                    'feels_like': data['main']['feels_like'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                    'humidity': data['main']['humidity'],
                    'clouds': data['clouds']['all'],
                    'visibility': data['visibility'],
                    'wind_speed': data['wind']['speed'],
                    'sunrise': datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
                    'sunset': datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S'),
                    'coordinates': f"({data['coord']['lat']}, {data['coord']['lon']})",
                }
                return weather_info
            else:
                raise ValueError("City not found.")
        else:
            # Raise an exception if the response is not successful
            raise ValueError("Unable to fetch weather data.")
    
    except requests.exceptions.RequestException as e:
        # Handle network-related or API request exceptions
        print(f"Request failed: {e}")
        raise ValueError("An error occurred while fetching weather data.")
    except ValueError as e:
        # Handle case when city is not found or other validation errors
        print(f"Error: {e}")
        raise ValueError(f"Error: {e}")

def home(request):
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        try:
            weather_info = get_weather_data(city_name)
            if weather_info:
                return render(request, 'weather/index.html', {'weather_info': weather_info})
        except ValueError as e:
            # Flash a message to the user if an exception is raised
            messages.error(request, str(e))  # Display the error message to the user
            return render(request, 'weather/index.html')
    return render(request, 'weather/index.html')
