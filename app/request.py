import requests
from settings import get_api_token

async def current_weather(city: str) -> dict:
    api_key = await get_api_token() 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    return response.json()


async def forecast_weather(city: str) -> dict:
    api_key = await get_api_token() 
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    return response.json()