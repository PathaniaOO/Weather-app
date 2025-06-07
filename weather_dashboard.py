import streamlit as st
import requests

# Set your OpenWeather API key here
API_KEY = "e282140472cd753c65cc3c2bce814ef3"

# Set up the app
st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="centered")
st.title("🌦️ Weather Dashboard")
st.subheader("Get real-time weather data by city")

# City input
city = st.text_input("Enter city name:")

# Weather fetching function
def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    return response.json()

# If user submits a city name
if city:
    data = get_weather(city, API_KEY)

    if data.get("cod") != 200:
        st.error(f"Error: {data.get('message', 'Invalid city name')}")
    else:
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        st.success(f"Weather in {city.capitalize()}")
        st.metric("🌡️ Temperature", f"{temp} °C")
        st.metric("💧 Humidity", f"{humidity}%")
        st.metric("💨 Wind Speed", f"{wind_speed} m/s")
        st.write(f"📝 Condition: **{weather}**")
