import os
from dotenv import load_dotenv
from weather_gui import WeatherApp
import tkinter as tk

load_dotenv()

api_key = os.getenv("OPENWEATHERMAP_API_KEY")

def main():

    root = tk.Tk()

    app = WeatherApp(root, api_key)

    root.mainloop()

if __name__ == "__main__":
    main()
