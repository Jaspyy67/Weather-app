import os
import tkinter as tk
from tkinter import messagebox
from weather import get_weather
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime

class WeatherApp:
    def __init__(self, root, api_key):
        self.api_key = api_key
        self.root = root
        self.root.title("Weather App")
        self.root.config(bg="skyblue")

        self.create_widgets()

    def create_widgets(self):
        self.input_frame = tk.Frame(self.root, bg="skyblue")
        self.input_frame.grid(row=0, column=0, pady=20, padx=20)

        self.city_label = tk.Label(self.input_frame, text="Enter city name:", font=("Helvetica", 14), bg="skyblue", fg="white")
        self.city_label.grid(row=0, column=0, pady=5)

        self.city_entry = tk.Entry(self.input_frame, width=30, font=("Helvetica", 14))
        self.city_entry.grid(row=1, column=0, pady=5)

        self.fetch_button = tk.Button(self.input_frame, text="Get Weather", font=("Helvetica", 12), command=self.show_weather, bg="#4CAF50", fg="white", relief="raised", width=20)
        self.fetch_button.grid(row=2, column=0, pady=10)

        self.weather_frame = tk.Frame(self.root, bg="skyblue")
        self.weather_frame.grid(row=1, column=0, pady=20, padx=20)

        self.weather_display = tk.Text(self.weather_frame, width=40, height=10, wrap=tk.WORD, padx=10, pady=10, font=("Courier", 10), bg="white", fg="black")
        self.weather_display.grid(row=0, column=0)

        self.weather_display.config(state=tk.DISABLED)


        self.forecast_frame = tk.Frame(self.root, bg="skyblue")
        self.forecast_frame.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.forecast_button = tk.Button(self.forecast_frame, text="Show 3-Day Forecast", font=("Helvetica", 12), command=self.show_forecast, bg="#FF9800", fg="white", relief="raised")
        self.forecast_button.grid(row=0, column=0, padx=10, pady=10)


        self.icon_frame = tk.Frame(self.root, bg="skyblue")
        self.icon_frame.grid(row=3, column=0, pady=10)

        self.icon_label = tk.Label(self.icon_frame, bg="skyblue")
        self.icon_label.grid(row=0, column=0)


        self.loading_label = tk.Label(self.root, text="Loading...", font=("Helvetica", 14), fg="blue", bg="skyblue")
        self.loading_label.grid(row=4, column=0, pady=10)
        self.loading_label.grid_remove() 
    def show_weather(self):
        city = self.city_entry.get()
        
        if city:
            self.loading_label.grid()  
            weather_info, icon_url = get_weather(city, self.api_key, forecast=False)  
            self.loading_label.grid_remove()  
            
            self.weather_display.config(state=tk.NORMAL)
            self.weather_display.delete(1.0, tk.END)
            self.weather_display.insert(tk.END, weather_info)
            self.weather_display.config(state=tk.DISABLED)
            
            self.display_icon(icon_url)
        else:
            messagebox.showerror("Input Error", "Please enter a city name.")

    def show_forecast(self):
        city = self.city_entry.get()
        
        if city:
            self.loading_label.grid() 
            forecast_info = get_weather(city, self.api_key, forecast=True) 
            self.loading_label.grid_remove()  
            
            self.weather_display.config(state=tk.NORMAL)
            self.weather_display.delete(1.0, tk.END)
            self.weather_display.insert(tk.END, forecast_info)
            self.weather_display.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Input Error", "Please enter a city name.")

    def display_icon(self, icon_url):
        try:
            response = requests.get(icon_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((50, 50))
            photo = ImageTk.PhotoImage(img)
            self.icon_label.config(image=photo)
            self.icon_label.image = photo
        except:
            print("Error fetching weather icon.")
