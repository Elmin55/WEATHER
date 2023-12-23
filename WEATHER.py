import requests

API_KEY = '45227d46ee50ed501779eeab26c62bf7'

def get_weather_data(city):
    try:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}"
            , timeout=5)
        weather_data.raise_for_status()
        return weather_data.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch weather data for {city}. {e}")
        return None

def display_weather_info(city, weather_data):
    if weather_data:
        weather = weather_data['weather'][0]['main']
        temp = weather_data['main']['temp']

        unit_choice = input('Enter temperature unit (C for Celsius, F for Fahrenheit): ').upper()

        if unit_choice == 'C':
            temp_result = round((temp - 32) * (5 / 9))
            unit_symbol = 'ºC'
        elif unit_choice == 'F':
            temp_result = round(temp)
            unit_symbol = 'ºF'
        else:
            print("Invalid choice. Defaulting to Celsius.")
            temp_result = round((temp - 32) * (5 / 9))
            unit_symbol = 'ºC'

        print(f"The Weather In {city} Is: {weather}")
        print(f"The Temperature In {city} Is: {temp_result}{unit_symbol}")
        
        
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        print(f"Humidity in {city}: {humidity}%")
        print(f"Wind Speed in {city}: {wind_speed} mph")

def main():
    user_input = input('Enter City: ')
    weather_data = get_weather_data(user_input)
    display_weather_info(user_input, weather_data)

if __name__ == "__main__":
    main()
