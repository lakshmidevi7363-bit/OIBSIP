# BMI Calculator

A Python-based BMI Calculator developed as part of the Oasis Infobyte Python Programming Internship.

## Features

- Calculate Body Mass Index (BMI)
- Display BMI category
- Store BMI records using SQLite
- View previous BMI records
- Display BMI trends using a graph
- Input validation
- Error handling
- Simple graphical user interface

## Technologies Used

- Python
- Tkinter
- SQLite
- Matplotlib

## Project Structure

```text
Python-Task2-BMICalculator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── main-interface.png
│   ├── bmi-result.png
│   ├── bmi-history.png
│   └── bmi-trend.png
│
└── venv/
```

The `venv` directory is a local Python virtual environment and is excluded from GitHub using `.gitignore`.

## Installation

### 1. Clone the Repository

Clone the OIBSIP repository from GitHub and open the BMI Calculator project folder.

```bash
git clone https://github.com/lakshmidevi7363-bit/OIBSIP.git
cd OIBSIP/Python-Task2-BMICalculator
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Make sure the virtual environment is activated and run:

```bash
python app.py
```

The BMI Calculator window will open.

## Database

The application automatically creates a SQLite database named:

```text
bmi_records.db
```

The database stores:

- User name
- Weight
- Height
- BMI
- BMI category
- Date and time of calculation

The database file is excluded from GitHub using `.gitignore`.

## Screenshots

### Main Interface

![Main Interface](./screenshots/main-interface.png)

### BMI Result

![BMI Result](./screenshots/bmi-result.png)

### BMI History

![BMI History](./screenshots/bmi-history.png)

### BMI Trend

![BMI Trend](./screenshots/bmi-trend.png)

## Input Validation

The application handles:

- Empty user names
- Non-numeric weight values
- Non-numeric height values
- Negative weight values
- Zero or negative height values
- Database read/write errors

## Future Improvements

- Height input in centimeters
- Export BMI history to CSV
- User profile management
- Dark mode
- Improved graphical dashboard
- Additional health metrics
