# OIBSIP – Python Programming Internship

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Internship](https://img.shields.io/badge/Internship-Oasis%20Infobyte-orange)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

## About

This repository contains the projects completed as part of my **Python Programming Internship at Oasis Infobyte (OIBSIP)**.

The internship focuses on developing practical Python programming skills through hands-on projects involving graphical user interfaces, APIs, user input handling, data processing, and application development.

Each task is organized in a separate folder with its source code, documentation, requirements, and screenshots.

---

## Internship Tasks

### Task 2 – BMI Calculator

A graphical BMI Calculator developed using Python and Tkinter.

#### Features

- Accepts user name, weight, and height
- Calculates Body Mass Index (BMI)
- Displays BMI category
- Stores BMI records using SQLite
- Displays BMI history
- Provides BMI trend visualization
- User-friendly graphical interface

**Technologies:**
- Python
- Tkinter
- SQLite
- Matplotlib

📁 [View BMI Calculator](./Python-Task2-BMICalculator/)

---

### Task 3 – Random Password Generator

A Python-based Random Password Generator that allows users to create customizable and secure passwords.

#### Features

- Custom password length
- Lowercase letters
- Uppercase letters
- Numbers
- Special characters
- Password generation
- Copy generated password to clipboard
- Input validation
- User-friendly Tkinter interface

**Technologies:**
- Python
- Tkinter
- Random
- String
- Pyperclip

📁 [View Random Password Generator](./Python-Task3-RandomPasswordGenerator/)

---

### Task 4 – Weather Application

A Python-based Weather Application that retrieves real-time weather information using the OpenWeather API.

#### Features

- Search weather by city name
- Displays temperature
- Displays feels-like temperature
- Displays humidity
- Displays atmospheric pressure
- Displays wind speed
- Displays weather condition
- Handles invalid city names
- Uses environment variables for API key security
- Simple Tkinter interface

**Technologies:**
- Python
- Tkinter
- Requests
- python-dotenv
- OpenWeather API

📁 [View Weather Application](./Python-Task4-WeatherApplication/)

---

## Repository Structure

```text
OIBSIP/
│
├── Python-Task2-BMICalculator/
│   ├── screenshots/
│   ├── app.py
│   ├── README.md
│   └── requirements.txt
│
├── Python-Task3-RandomPasswordGenerator/
│   ├── screenshots/
│   ├── app.py
│   ├── README.md
│   └── requirements.txt
│
├── Python-Task4-WeatherApplication/
│   ├── screenshots/
│   ├── app.py
│   ├── README.md
│   └── requirements.txt
│
├── .gitignore
└── README.md

Technologies Used
Technology	Purpose
Python	Core programming language
Tkinter	Graphical User Interface
SQLite	Database management
Matplotlib	Data visualization
Requests	API requests
python-dotenv	Environment variable management
Pyperclip	Clipboard operations
OpenWeather API	Real-time weather data
Git & GitHub	Version control and project hosting
Key Learning Outcomes

Through these projects, I gained practical experience in:

Python application development
GUI development using Tkinter
Functions and modular programming
Exception handling
User input validation
File and database handling
SQLite database integration
Data visualization
Working with REST APIs
Environment variables and API key security
Dependency management using requirements.txt
Git and GitHub version control
Project documentation
How to Run the Projects
1. Clone the Repository
git clone https://github.com/lakshmidevi7363-bit/OIBSIP.git
2. Navigate to a Task

For example:

cd OIBSIP/Python-Task4-WeatherApplication
3. Create a Virtual Environment
python3 -m venv venv
4. Activate the Virtual Environment

On macOS/Linux:

source venv/bin/activate

On Windows:

venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
6. Run the Application
python app.py
API Key Security

The Weather Application uses an OpenWeather API key.

The API key is stored in a .env file and is intentionally excluded from Git using .gitignore.

Example:

OPENWEATHER_API_KEY=your_api_key_here

Never commit or publicly share your actual API key.

Screenshots

Screenshots demonstrating the functionality of each project are available inside the respective project folders.

BMI Calculator Screenshots
Random Password Generator Screenshots
Weather Application Screenshots
Internship

Organization: Oasis Infobyte
Program: Python Programming Internship
Repository: OIBSIP

Author

Lakshmi Devi R

Python Programming Intern

Acknowledgement

I would like to thank Oasis Infobyte for providing the opportunity to work on these practical Python programming projects and gain hands-on experience in application development.

⭐ Thank you for visiting this repository!
