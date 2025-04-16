import pandas as pd
from modules import datetime_utils, weather, config
from modules.config import API_PARAMS, MONTHS_EN, WEATHER_DESCRIPTIONS

def main():
    # Get and format time
    current_time = datetime_utils.get_brasilia_time()
    datetime_info = datetime_utils.format_datetime(current_time, MONTHS_EN)
    
    # Get weather data
    client = weather.setup_api_client()
    weather_data = weather.get_weather_data(client, API_PARAMS)
    
    # Generate README content
    readme_content = f""" # Today's Date and Weather
    
## Date and Time
{datetime_info['formatted_date']} 📅
{datetime_info['formatted_time']} (GMT-3) 🕒

## Current Season
{datetime_info['season']}
## Weather 
**Conditions:** {WEATHER_DESCRIPTIONS.get(weather_data['weather_code'], 'N/A')}
**Temperature:** {weather_data['temperature']:.1f}°C  
**Humidity:** {weather_data['humidity']}%  
**Last Updated (D/M/Y):** {current_time.strftime('%d/%m/%Y %H:%M')}
##
<br>
<div align="center">Inspired by <a href="https://github.com/leimao/What-Is-The-Date-Today">leimao's repository</a></div>
"""
    
    # Save outputs in the README.md file
    with open('README.md', 'w') as f:
        f.write(readme_content)
    # Saves it to csv format
    pd.DataFrame({
        'date': [current_time],
        'temperature': [weather_data['temperature']],
        'humidity': [weather_data['humidity']],
        'weather_code': [weather_data['weather_code']]
    }).to_csv('data/weather_data.csv', index=False)

if __name__ == "__main__":
    main()
