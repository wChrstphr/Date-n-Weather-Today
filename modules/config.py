# API Configuration
OPENMETEO_URL = "https://api.open-meteo.com/v1/forecast"
LOCATION = {
    "latitude": -23.5505,
    "longitude": -46.6333,
    "timezone": "America/Sao_Paulo"
}

# Time Formatting
TIMEZONE = "America/Sao_Paulo"
DATE_FORMAT = "%B %d, %Y"  # Ex: "December 25, 2023"

# Weather description (For future implementation)
WEATHER_DESCRIPTIONS = {
    0: "Clear sky ☀️",
    1: "Mainly clear 🌤",
    2: "Partly cloudy ⛅",
    3: "Overcast ☁️",
    45: "Fog 🌫",
    61: "Light rain 🌧",
    80: "Rain showers 🌦"
}
