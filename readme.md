# Multi-Tool Assistant

**Multi-Tool Assistant** is an intelligent assistant application that integrates multiple tools to enhance productivity and provide real-time information. This project leverages LangChain for agent-based task management, enabling users to interact with a variety of services, including weather updates, to-do list management, event calendar, and EV charging station finder.

## Features

- **Weather Information**: Get real-time weather updates for any city using the OpenWeatherMap API.
- **To-Do List Manager**: Add tasks to your to-do list and view all tasks.
- **Event Calendar**: Add events to your calendar and view them.
- **EV Charging Station Finder**: Find Electric Vehicle (EV) charging stations near a given city.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.x
- `pip` (Python package manager)
- `.env` file containing your API keys

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/multi-tool-assistant.git
   cd multi-tool-assistant
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
   ```

   You can get the `WEATHER_API_KEY` from [OpenWeatherMap](https://openweathermap.org/api).

4. **Run the application**:

   ```bash
   python app.py
   ```

   This will start the assistant, and you can interact with it in the console.

## How to Use

Once the application is running, the assistant will prompt you for input. You can ask the assistant to:

- Get the current weather of a city (e.g., "What is the weather in London?").
- Add tasks to your to-do list (e.g., "Add 'Buy groceries' to my to-do list").
- View all tasks in your to-do list (e.g., "Show me my tasks").
- Add events to your calendar (e.g., "Add 'Doctor's appointment' to my calendar").
- Find EV charging stations near a city (e.g., "Where are the EV charging stations in San Francisco?").

To exit the application, simply type `exit`.

## Tools

This project integrates the following tools:

- **Weather Tool**: Fetches real-time weather data from OpenWeatherMap.
- **To-Do List Manager**: Manages tasks for your to-do list.
- **Calendar Manager**: Adds and displays events on your calendar.
- **EV Charging Station Finder**: Finds nearby EV charging stations using the RapidAPI EV Charge Finder service.

## Technologies Used

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

```