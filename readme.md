# Multi-Tool Assistant API

**Multi-Tool Assistant API** is a FastAPI-based backend that integrates multiple services and tools, providing users with functionalities like weather updates, task management, event calendar, and EV charging station finder. The API leverages LangChain for agent-based task management, enabling seamless interaction with various services.

## Features

- **Weather Information**: Get real-time weather updates for any city using the OpenWeatherMap API.
- **To-Do List Manager**: Add tasks to your to-do list, view, and delete tasks.
- **Event Calendar**: Add events to your calendar and view them.
- **EV Charging Station Finder**: Find Electric Vehicle (EV) charging stations near a given city.

## Prerequisites

Before running the API, ensure you have:

- Python 3.x
- `pip` (Python package manager)
- A `.env` file with your API keys

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/gautamraj8044/multi-tool-assistant.git
   cd multi-tool-assistant
   ```

2. **Install dependencies**:
   Create a virtual environment (recommended) and install the required libraries:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory with the following:
   ```bash
   WEATHER_API_KEY=your_openweathermap_api_key
   x-rapidapi-key=your_rapidapi_key
   ```
   Obtain `WEATHER_API_KEY` from OpenWeatherMap and `x-rapidapi-key` from RapidAPI EV Charge Finder.

4. **Run the API**:
   Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```

   The server will be available at `http://127.0.0.1:8000`.

## API Endpoints

### /assist/
- **Method**: GET
- **Description**: Handles user queries by invoking a LangChain agent to use various tools for responses.
- **Query Parameters**:
  - `user_input`: A string representing the user's query (e.g., "What is the weather in New York?").
  
- **Response**:
  A JSON object with the agent's response.
  ```json
  {
    "response": "The current weather in New York is clear sky with a temperature of 25°C."
  }
  ```

## Usage Examples

1. **Weather Query**: 
   - Request: `GET /assist/?user_input=What%20is%20the%20weather%20in%20London?`
   - Response: Current weather details for London.

2. **Task Management**:
   - Add Task: `GET /assist/?user_input=Add%20'Buy%20groceries'%20to%20my%20to-do%20list`
   - View Tasks: `GET /assist/?user_input=Show%20me%20my%20tasks`

3. **Event Calendar**:
   - Add Event: `GET /assist/?user_input=Add%20'Doctor%27s%20appointment'%20to%20my%20calendar`

4. **EV Charging Stations**:
   - Find Stations: `GET /assist/?user_input=Where%20are%20the%20EV%20charging%20stations%20in%20San%20Francisco?`

## Tools

- **Weather Tool**: Uses OpenWeatherMap API for weather data.
- **To-Do List Manager**: Manages tasks in an SQLite database.
- **Calendar Manager**: Basic in-memory event storage.
- **EV Charging Station Finder**: Utilizes RapidAPI for EV station data.

## Technologies Used

- **FastAPI**: API framework.
- **LangChain**: For tool integration and agent management.
- **SQLite**: For task storage.
- **OpenWeatherMap API & RapidAPI**: External data services.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## Contact

For questions or feedback, open an issue or contact [gautamraj8044@gmail.com](mailto:gautamraj8044@gmail.com).
```