# Multi-Tool Assistant API

**Multi-Tool Assistant API** is a FastAPI-based backend that integrates multiple services and tools, providing users with a set of functionalities like weather updates, task management, event calendar, and EV charging station finder. The API leverages LangChain for agent-based task management, enabling users to interact with various services seamlessly.

## Features

- **Weather Information**: Get real-time weather updates for any city using the OpenWeatherMap API.
- **To-Do List Manager**: Add tasks to your to-do list and view all tasks.
- **Event Calendar**: Add events to your calendar and view them.
- **EV Charging Station Finder**: Find Electric Vehicle (EV) charging stations near a given city.

## Prerequisites

Before running the API, ensure you have the following:

- Python 3.x
- `pip` (Python package manager)
- `.env` file containing your API keys

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/multi-tool-assistant-api.git
   cd multi-tool-assistant-api
   ```

2. **Install dependencies**:

   Create a virtual environment (recommended) and install the required Python libraries:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   Create a `.env` file in the root directory and add the following API keys:

   ```bash
   WEATHER_API_KEY=your_openweathermap_api_key
   x-rapidapi-key=your_rapidapi_key
   ```

   You can get the `WEATHER_API_KEY` from [OpenWeatherMap](https://openweathermap.org/api) and the `x-rapidapi-key` from [RapidAPI EV Charge Finder](https://rapidapi.com/).

4. **Run the API**:

   Start the FastAPI server:

   ```bash
   uvicorn app:app --reload
   ```

   The server will be running at `http://127.0.0.1:8000`.

## API Endpoints

### `/assist/`

**Method**: `GET`

**Description**: This endpoint takes user input and returns an intelligent response by invoking a LangChain agent, which can use various tools like weather, to-do list, calendar, and EV charging station finder.

**Query Parameters**:

- `user_input`: A string containing the user query (e.g., "What is the weather in New York?").

**Response**:

- A JSON object with the response from the LangChain agent.

```json
{
  "response": "The current weather in New York is clear sky with a temperature of 25°C."
}
```

## How to Use

Once the API is running, you can interact with it via HTTP requests to the `/assist/` endpoint:

- To get the current weather of a city:
  - **Request**: `GET /assist/?user_input=What%20is%20the%20weather%20in%20London?`
  - **Response**: The current weather details for London.

- To add a task to your to-do list:
  - **Request**: `GET /assist/?user_input=Add%20'Buy%20groceries'%20to%20my%20to-do%20list`
  - **Response**: Confirmation message that the task has been added.

- To view all tasks in your to-do list:
  - **Request**: `GET /assist/?user_input=Show%20me%20my%20tasks`
  - **Response**: List of all tasks in your to-do list.

- To add an event to your calendar:
  - **Request**: `GET /assist/?user_input=Add%20'Doctor%27s%20appointment'%20to%20my%20calendar`
  - **Response**: Confirmation message that the event has been added.

- To find EV charging stations near a city:
  - **Request**: `GET /assist/?user_input=Where%20are%20the%20EV%20charging%20stations%20in%20San%20Francisco?`
  - **Response**: List of EV charging stations near San Francisco.

## Tools

This API integrates the following tools:

- **Weather Tool**: Fetches real-time weather data from OpenWeatherMap.
- **To-Do List Manager**: Manages tasks for your to-do list.
- **Calendar Manager**: Adds and displays events on your calendar.
- **EV Charging Station Finder**: Finds nearby EV charging stations using the RapidAPI EV Charge Finder service.

## Technologies Used

- **FastAPI**: For building the API.
- **LangChain**: For integrating and managing multiple tools.
- **OpenWeatherMap API**: For fetching weather data.
- **RapidAPI**: For fetching EV charging station information.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## Contact

For any questions or feedback, feel free to open an issue or reach out to me at [gautamraj8044@gmail.com].

---