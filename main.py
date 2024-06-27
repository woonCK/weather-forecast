import requests
from pprint import pprint

API_KEY = '633edf23fe2bf0896ebc6769deab9848'

def main():
    # print("Hello World!")
    city = input("Enter a city: ")
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

    weather_data = requests.get(base_url).json()

    pprint(weather_data)
    
if __name__ == "__main__":
    main()