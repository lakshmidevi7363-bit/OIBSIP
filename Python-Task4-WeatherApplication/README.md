# Weather Application

A Python-based Weather Application that fetches real-time weather information using the OpenWeather API.

## Features

- Search weather by city name
- Displays current temperature
- Displays feels-like temperature
- Displays humidity
- Displays atmospheric pressure
- Displays wind speed
- Displays weather condition
- Handles invalid city names
- Simple and user-friendly Tkinter interface

## Technologies Used

- Python
- Tkinter
- Requests
- python-dotenv
- OpenWeather API

## Project Structure

```text
Python-Task4-WeatherApplication/
│
├── screenshots/
│   ├── main-interface.png
│   ├── chennai-weather.png
│   ├── mumbai-weather.png
│   └── invalid-city.png
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

How to Run
1. Clone the repository
git clone https://github.com/lakshmidevi7363-bit/OIBSIP.git
2. Navigate to the project
cd OIBSIP/Python-Task4-WeatherApplication
3. Create a virtual environment
python3 -m venv venv
4. Activate the virtual environment

On macOS/Linux:

source venv/bin/activate
5. Install dependencies
pip install -r requirements.txt
6. Configure the API key

Create a .env file and add:

OPENWEATHER_API_KEY=your_api_key_here

Replace your_api_key_here with your own OpenWeather API key.

7. Run the application
python app.py
Screenshots
Main Interface

Chennai Weather

Mumbai Weather

Invalid City

Security

The OpenWeather API key is stored in a .env file and should not be committed to GitHub.

Future Improvements
Weather forecast for multiple days
Weather icons
Automatic location detection
Temperature unit selection
More detailed weather information
Improved user interface
