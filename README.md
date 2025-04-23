# Weather App

A straightforward, real-time weather application that delivers current conditions and forecasts with simplicity and accuracy.

## Description

Weather App is a no-frills solution for accessing weather information quickly. Built with the OpenWeatherMap API, it provides users with essential weather data without unnecessary complexity. Whether you need to check current conditions or plan for the next few days, Weather App delivers reliable meteorological information in a clean, accessible format.

## Why This App?

In a world of cluttered weather applications with excessive features, Weather App focuses on what matters most - delivering accurate weather information efficiently. It was created to solve the common problem of having to navigate through complicated interfaces just to answer simple questions like "Do I need an umbrella today?" or "How cold will it be tomorrow evening?"

## Features

### Current Weather Display
Get instant access to important weather metrics:
* Temperature in Celsius
* Humidity percentage
* Weather description
* Wind speed in m/s
* "Feels like" temperature
* Barometric pressure in hPa
* Sunrise and sunset times

### 3-Day Forecast
Plan ahead with a concise forecast featuring:
* Weather predictions for the next 3 days
* Three time slots per day (Morning 6AM, Afternoon 12PM, Evening 6PM)
* Temperature readings for each time slot
* Weather descriptions for each period
* Weather condition icons


## Quick Start

```bash
### Clone the repo

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app

# Install dependencies
pip install -r requirements.txt

# Set up your API key
export OPENWEATHER_API_KEY="your_api_key_here"

# Run the application
python main.py
```markdown

## 🤝 Contributing

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. Set up the environment
(Optional but recommended to use a virtual environment)
```bash
# Create and activate a virtual environment
python -m venv venv

# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API key
Set your OpenWeatherMap API key as an environment variable:

```bash
# On macOS/Linux
export OPENWEATHER_API_KEY="your_api_key_here"

# On Windows
set OPENWEATHER_API_KEY="your_api_key_here"
```

### 5. Run the application
```bash
python main.py
```

### 6. Run the tests
```bash
pytest
```

### 7. Submit a pull request
To contribute to the Weather App:

1. **Fork** the repository
2. **Create** a feature branch:
    ```bash
    git checkout -b feature/amazing-feature
    ```
3. **Commit** your changes:
    ```bash
    git commit -m 'Add some amazing feature'
    ```
4. **Push** to your branch:
    ```bash
    git push origin feature/amazing-feature
    ```
5. **Open a Pull Request** to the main branch
