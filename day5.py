import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
while True:
    city_name = input("enter the name of the city (or 'exit' to quit): ")
    if city_name.lower() == "exit":
        break
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity:{main['humidity']}%")
        print(f"Wind Speed: {wind['speed'] * 3.6:.1f} km/h")
        print(f"Weather: {weather['description']}")
    else:
        print("City Not Found")
        break
