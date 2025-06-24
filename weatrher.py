import requests

def weather_detail(city):
    api_key = "247c052b2ce84ac59389ee0d3da25784"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        temprature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]

        print(f"Weather in {city}")
        print(f"Temperature: {temprature}°C (feels like: {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Description: {data['weather'][0]['description'].capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the weather data: {e}")
    except KeyError:
        print("ERROR: Unable to parse data (maybe wrong city)")

city = input("Enter the name of the city: ")
weather_detail(city)
