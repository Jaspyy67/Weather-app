import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    api_key = "your_openweathermap_api_key_here"  # Replace with your own API key

    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Sending request to OpenWeatherMap
        response = requests.get(url)
        data = response.json()

        # Check if the city was found
        if data["cod"] != "404":
            main_data = data["main"]
            weather_data = data["weather"][0]

            # Extracting data
            temperature = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            weather_description = weather_data["description"]

            # Display the weather information in the label
            result_label.config(
                text=f"Temperature: {temperature}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_description.capitalize()}"
            )
        else:
            # Show error message if city not found
            messagebox.showerror("Error", "City not found, please try again.")

    except requests.exceptions.RequestException:
        # Show error message for network issues
        messagebox.showerror("Error", "Could not fetch weather data. Please try again later.")

# Set up the main window
root = tk.Tk()
root.title("Weather App")

# Set up the entry field for the city
city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=5)

# Set up the button to fetch weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Set up the label to display weather information
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
