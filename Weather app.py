import requests

def get_weather(city):
    API_KEY = "5b5b39a306fbce7e4bc267ab8a223439"  # Replace with your OpenWeatherMap API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] == 200:
            print(f"\n Weather in {data['name']}, {data['sys']['country']}:")
            print(f" Temperature: {data['main']['temp']}°C")
            print(f" Condition: {data['weather'][0]['description'].capitalize()}")
            print(f" Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f" City not found. ({data['message']})")
    except Exception as e:
        print(" Error:", e)

# Run
print(" Weather App")
city_name = input("Enter city name: ")
get_weather(city_name)
