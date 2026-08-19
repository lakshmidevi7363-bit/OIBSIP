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

> The `.env` file contains the API key and is excluded from GitHub using `.gitignore`.

## Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/lakshmidevi7363-bit/OIBSIP.git
```

### 2. Navigate to the Project

```bash
cd OIBSIP/Python-Task4-WeatherApplication
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the API Key

Create a `.env` file inside the project folder and add:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own OpenWeather API key.

### 7. Run the Application

```bash
python app.py
```

The Weather Application window will open.

### Screenshots

- [Main Interface](./screenshots/main-interface.png)
- [Chennai Weather](./screenshots/chennai-weather.png)
- [Mumbai Weather](./screenshots/mumbai-weather.png)
- [Invalid City](./screenshots/invalid-city.png)

## Security

The OpenWeather API key is stored in a `.env` file and should not be committed to GitHub.

The `.env` file is excluded using `.gitignore`.

> Never share your actual API key publicly.

## Future Improvements

- Weather forecast for multiple days
- Weather icons
- Automatic location detection
- Temperature unit selection
- More detailed weather information
- Improved user interface
