import os
import httpx
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# Ensure OPENROUTER_API_KEY is set in environment variables

@tool
def get_weather(city_name: str):
    """Get the current weather for a given city name."""
    # First, get coordinates for the city
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
    
    try:
        geo_response = httpx.get(geocoding_url, params=params)
        geo_data = geo_response.json()
        
        if not geo_data.get("results"):
            return f"Could not find coordinates for {city_name}."
            
        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        
        # Now get weather
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "weather_code"]
        }
        
        weather_response = httpx.get(weather_url, params=weather_params)
        weather_data = weather_response.json()
        
        if "current" in weather_data:
            current = weather_data["current"]
            temp = current["temperature_2m"]
            unit = weather_data["current_units"]["temperature_2m"]
            return f"The current temperature in {city_name} is {temp}{unit}."
        else:
            return f"Could not fetch weather data for {city_name}."
            
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

def get_agent_executor():
    llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPENROUTER_API_KEY"),
        model="openai/gpt-3.5-turbo",
    )
    
    tools = [get_weather]
    
    # LangGraph prebuilt agent
    agent_executor = create_react_agent(llm, tools)
    
    return agent_executor
