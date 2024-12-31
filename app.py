from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import requests
import os
import json

# Load environment variables from .env file
load_dotenv()

# Fetching the Weather API Key from environment variables
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Function to fetch and return weather data for a given location
def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The current weather in {location} is {weather_desc} with a temperature of {temp}°C."
    else:
        return "Sorry, I couldn't fetch the weather for that location."

# To-Do list functionality: Add and show tasks
todo_list = []
event_list = []

def add_task(task):
    todo_list.append(task)
    return f"Task '{task}' added to your To-Do list!"

def show_tasks():
    if not todo_list:
        return "Your To-Do list is empty."
    return "\n".join([f"{i + 1}. {task}" for i, task in enumerate(todo_list)])

# Basic calendar functionality: Add and show events
def add_event(event):
    return f"Event '{event}' has been added to your calendar!"

def show_events():
    if not event_list:
        return "Your calendar is empty."
    return "\n".join([f"{i + 1}. {event}" for i, event in enumerate(event_list)])

# Function to fetch EV charging stations near a given city
def get_ev_charging_stations(city):
    url = "https://ev-charge-finder.p.rapidapi.com/search-by-location"
    querystring = {"near": city, "limit": "20"}
    headers = {
        "x-rapidapi-key": "bea4fbecfamsh387f15bb64e582bp142354jsncf45b337573e",
        "x-rapidapi-host": "ev-charge-finder.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        stations_info = []
        for station in data['data']:
            station_name = station['name']
            station_info = f"Station Name: {station_name}\n"
            for connector in station['connectors']:
                station_info += f"  Connector Type: {connector['type']}\n"
                station_info += f"    Total: {connector['total']}\n"
                
                # Handle missing 'kw' or 'speed' key gracefully
                kw = connector.get('kw', 'N/A')
                station_info += f"    kW: {kw}\n"
                
                speed = connector.get('speed', 'N/A')
                station_info += f"    Speed: {speed}\n"
                
            stations_info.append(station_info)
        return "\n\n".join(stations_info)
    else:
        return "Sorry, I couldn't fetch EV charging stations for that location."

# Define tools for LangChain agent to interact with
tools = [
    Tool(
        name="Weather Tool",
        func=lambda location: get_weather(location),
        description="Use this tool to get the current weather in any location.",
    ),
    Tool(
        name="To-Do List Manager",
        func=lambda task: add_task(task),
        description="Use this tool to add tasks to your To-Do list.",
    ),
    Tool(
        name="Show To-Do List",
        func=lambda _: show_tasks(),
        description="Use this tool to view all tasks in your To-Do list.",
    ),
    Tool(
        name="Calendar Manager",
        func=lambda event: add_event(event),
        description="Use this tool to add events to your calendar.",
    ),
    Tool(
        name="Show Calendar",
        func=lambda _: show_events(),
        description="Use this tool to view all events in your calendar.",
    ),
    Tool(
        name="EV Charging Station Finder",
        func=lambda city: get_ev_charging_stations(city),
        description="Use this tool to find EV charging stations near a given city.",
    ),
]

# Initialize the LLM (Language Model) and agent
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Example conversation loop with user input
while True:
    user_input = input("\nHow can I assist you? (Type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    response = agent.invoke(user_input)
    
    # Extract and print the response output
    response_str = response.get('output', '')  # Default to empty string if no 'output' key
    print("\n" + response_str)
