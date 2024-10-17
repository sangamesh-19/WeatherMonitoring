import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    """Fetch weather data for a specific city."""
    try:
        # Construct the API endpoint
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        
        # Make the GET request to the API
        response = requests.get(url)
        
        # Raise an error for bad responses
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant information
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
        }
        return weather_info
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    
    return None
