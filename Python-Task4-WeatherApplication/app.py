import tkinter as tk
from tkinter import ttk, messagebox
import requests
import os
from dotenv import load_dotenv



load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = city_var.get().strip()

    if not city:
        messagebox.showwarning("Input Required", "Please enter a city name.")
        return

    if not API_KEY:
        messagebox.showerror(
            "API Key Error",
            "OpenWeather API key is missing. Please check your .env file."
        )
        return

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 404:
            messagebox.showerror(
                "City Not Found",
                "Please enter a valid city name."
            )
            return

        if response.status_code == 401:
            messagebox.showerror(
                "API Error",
                "Invalid or inactive OpenWeather API key."
            )
            return

        response.raise_for_status()

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        condition = data["weather"][0]["description"].title()

        result_text.set(
            f"Weather in {city_name}, {country}\n\n"
            f"Condition: {condition}\n"
            f"Temperature: {temperature:.1f} °C\n"
            f"Feels Like: {feels_like:.1f} °C\n"
            f"Humidity: {humidity}%\n"
            f"Pressure: {pressure} hPa\n"
            f"Wind Speed: {wind_speed} m/s"
        )

    except requests.exceptions.Timeout:
        messagebox.showerror(
            "Connection Error",
            "The weather service took too long to respond."
        )

    except requests.exceptions.ConnectionError:
        messagebox.showerror(
            "Connection Error",
            "Please check your internet connection."
        )

    except requests.exceptions.RequestException as error:
        messagebox.showerror(
            "Error",
            f"Unable to retrieve weather data.\n\n{error}"
        )



root = tk.Tk()
root.title("Weather Application")
root.geometry("650x600")
root.resizable(False, False)


title_label = ttk.Label(
    root,
    text="WEATHER APPLICATION",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=30)


input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

city_label = ttk.Label(
    input_frame,
    text="Enter City:",
    font=("Arial", 14)
)
city_label.grid(row=0, column=0, padx=10)

city_var = tk.StringVar()

city_entry = ttk.Entry(
    input_frame,
    textvariable=city_var,
    width=30,
    font=("Arial", 14)
)
city_entry.grid(row=0, column=1, padx=10)


search_button = ttk.Button(
    root,
    text="Get Weather",
    command=get_weather
)
search_button.pack(pady=20)


result_frame = ttk.LabelFrame(
    root,
    text="Weather Details",
    padding=20
)
result_frame.pack(
    padx=40,
    pady=20,
    fill="both",
    expand=True
)

result_text = tk.StringVar()
result_text.set("Enter a city name and click 'Get Weather'.")

result_label = ttk.Label(
    result_frame,
    textvariable=result_text,
    font=("Arial", 14),
    justify="left"
)
result_label.pack(
    anchor="center",
    pady=30
)

city_entry.bind("<Return>", lambda event: get_weather())

root.mainloop()