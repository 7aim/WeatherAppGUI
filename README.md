# Weather App

A simple desktop Weather App built using Python's `tkinter` for the graphical interface and `requests` to access live weather data from the [OpenWeatherMap API](https://openweathermap.org/api).

## Overview

This Weather App allows users to input the name of a city and retrieve the current weather conditions including:
- **Country**
- **Weather description (main)**
- **Temperature (in °C)**

It serves as a beginner-friendly project showcasing how to interact with APIs and create GUIs using Python.

## Features

- **Real-time Weather Data:** Retrieves and displays current weather details for the specified city.
- **User-friendly GUI:** A minimalist design using `tkinter` with custom colors and fonts.
- **Error Handling:** If the city is not found, the application informs the user to enter a valid city.
- **Easy Customization:** Modify the colors, API key, or other UI components as needed.

## Screenshots

*(Optional: Add a screenshot of your application here if you have one.)*

## Prerequisites

Before running the Weather App, ensure you have the following:
- **Python 3.x** installed on your system.
- The Python packages:
  - [`requests`](https://pypi.org/project/requests/)
  - [`tkinter`](https://docs.python.org/3/library/tkinter.html) (usually comes pre-installed with Python)

You can install the `requests` package using pip:
```bash
pip install requests
