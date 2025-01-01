from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from database import create_table,add_task_to_db,show_tasks_from_db,delete_task
import requests
import os
import json

# Load environment variables
load_dotenv()

# Weather API Key
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Function to fetch weather data
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

create_table()
event_list=[]
search = DuckDuckGoSearchRun()
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

def add_task(task):
    return add_task_to_db(task)

def show_tasks():
    return show_tasks_from_db()


def delete_task_from_db(task_id):
    return delete_task(task_id)

# Calendar functionality (basic placeholder)
def add_event(event):
    event_list.append(event)
    return f"Event '{event}' has been added to your calendar!"

def show_events():
    if not event_list:
        return "Your calendar is empty."
    return "\n".join([f"{i + 1}. {event}" for i, event in enumerate(event_list)])

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
                
                # Safely handle missing 'kw' key
                kw = connector.get('kw', 'N/A')  # Use 'N/A' if 'kw' key is not present
                station_info += f"    kW: {kw}\n"
                
                # Safely handle missing 'speed' key
                speed = connector.get('speed', 'N/A')  # Use 'N/A' if 'speed' key is not present
                station_info += f"    Speed: {speed}\n"
                
            stations_info.append(station_info)
        return "\n\n".join(stations_info)
    else:
        return "Sorry, I couldn't fetch EV charging stations for that location."


tools = [
    Tool(
        name="Weather Tool",
        func=lambda location: get_weather(location),
        description="Get current weather in any location.",
    ),
    Tool(
        name="Add Task",
        func=lambda task: add_task(task),
        description="Add tasks to your To-Do list.",
    ),
    Tool(
        name="Show Tasks",
        func=lambda _: show_tasks(),
        description="View all tasks in your To-Do list.",
    ),
    Tool(
        name="Delete Task",
        func=lambda task_id: delete_task_from_db(task_id),
        description="Delete a task from your To-Do list.",
    ),
    Tool(
        name="DuckDuckGo Search",
        func=lambda query: search.run(query),
        description="Search for information using DuckDuckGo.",
    ),
    Tool(
        name="Wikipedia Search",
        func=lambda query: wikipedia.run(query),
        description="Search for information on Wikipedia.",
    ),
]

# Initialize the LLM (Language Model) and agent
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-8b")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True,handle_parsing_errors=True)

# FastAPI route to handle user input and get agent response
@app.get("/assist/")
async def assist(user_input: str):
    # Pass user input to the LangChain agent
    response = agent.invoke(user_input)
    
    # Extract and return the response output
    response_str = response.get('output', '')  # Default to empty string if no 'output' key
    return {"response": response_str}

# Run the app with: uvicorn filename:app --reload
