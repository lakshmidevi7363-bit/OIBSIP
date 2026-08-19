# OIBSIP – Python Programming Internship

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Oasis Infobyte](https://img.shields.io/badge/Oasis%20Infobyte-Internship-orange)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

## About

This repository contains the projects completed as part of my **Python Programming Internship at Oasis Infobyte (OIBSIP)**.

The internship focuses on developing practical Python programming skills through hands-on projects involving GUI development, API integration, database management, user input handling, and application development.

Each task is organized in a separate folder containing the source code, documentation, requirements, and screenshots.

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

#### Technologies Used

- Python
- Tkinter
- SQLite
- Matplotlib

**Project:** [Python-Task2-BMICalculator](./Python-Task2-BMICalculator/)

---

### Task 3 – Random Password Generator

A Python-based Random Password Generator that allows users to create customizable passwords.

#### Features

- Custom password length
- Lowercase letters
- Uppercase letters
- Numbers
- Special characters
- Password generation
- Copy generated password to clipboard
- Input validation
- User-friendly graphical interface

#### Technologies Used

- Python
- Tkinter
- Random
- String
- Pyperclip

**Project:** [Python-Task3-RandomPasswordGenerator](./Python-Task3-RandomPasswordGenerator/)

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
- Simple graphical interface

#### Technologies Used

- Python
- Tkinter
- Requests
- python-dotenv
- OpenWeather API

**Project:** [Python-Task4-WeatherApplication](./Python-Task4-WeatherApplication/)

---

## Repository Structure

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

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Tkinter | Graphical User Interface |
| SQLite | Database management |
| Matplotlib | Data visualization |
| Requests | API requests |
| python-dotenv | Environment variable management |
| Pyperclip | Clipboard operations |
| OpenWeather API | Real-time weather data |
| Git & GitHub | Version control and project hosting |

---

## Key Learning Outcomes

Through these projects, I gained practical experience in:

- Python application development
- GUI development using Tkinter
- Functions and modular programming
- Exception handling
- User input validation
- SQLite database integration
- Data visualization
- Working with REST APIs
- Environment variable management
- API key security
- Dependency management using `requirements.txt`
- Git and GitHub version control
- Project documentation

---

# ▶️ How to Run the Projects

## 1. Clone the Repository

```bash
git clone https://github.com/lakshmidevi7363-bit/OIBSIP.git
```

## 2. Navigate to a Project

For example, to run the Weather Application:

```bash
cd OIBSIP/Python-Task4-WeatherApplication
```

## 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

## 4. Activate the Virtual Environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the Application

```bash
python app.py
```

---

# 🔑 Weather Application API Key

The Weather Application uses the **OpenWeather API** to retrieve real-time weather information.

The API key is stored in a `.env` file and is excluded from Git using `.gitignore`.

Create a `.env` file inside the Weather Application folder:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

> ⚠️ **Important:** Never upload or publicly share your actual API key.

---

# 📸 Screenshots

Screenshots for each project are available inside their respective project folders.

### 🧮 BMI Calculator

[View BMI Calculator Screenshots](./Python-Task2-BMICalculator/screenshots/)

### 🔐 Random Password Generator

[View Random Password Generator Screenshots](./Python-Task3-RandomPasswordGenerator/screenshots/)

### 🌤️ Weather Application

[View Weather Application Screenshots](./Python-Task4-WeatherApplication/screenshots/)

---

# 📚 Project Documentation

Each project contains its own README file with detailed information about:

- Project overview
- Features
- Technologies used
- Installation
- How to run
- Project structure
- Screenshots
- Future improvements

---

# 👨‍💻 Internship Information

**Organization:** Oasis Infobyte  
**Program:** Python Programming Internship  
**Repository:** OIBSIP

---

# 👤 Author

**Lakshmi Devi R**

Python Programming Intern

---

# 🙏 Acknowledgement

I would like to thank **Oasis Infobyte** for providing me with the opportunity to work on these practical Python programming projects and gain hands-on experience in application development.

---

⭐ **Thank you for visiting this repository!**
