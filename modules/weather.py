import openmeteo_requests
import requests_cache
from retry_requests import retry

# Setup API client and make sure it loads the session correctly
def setup_api_client():
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    return openmeteo_requests.Client(session=retry_session)

# GET request
def get_weather_data(client, params):
    url = "https://api.open-meteo.com/v1/forecast"
    response = client.weather_api(url, params=params)[0]
    current = response.Current()
    return {
        "temperature": current.Variables(0).Value(),
        "humidity": current.Variables(1).Value(),
        "weather_code": current.Variables(2).Value()
    }
