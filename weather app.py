import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather details
def get_weather():
    city = city_entry.get()
    if city:
        try:
            api_key = 'your_openweathermap_api_key'  # Replace with your OpenWeatherMap API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if data['cod'] == 200:
                city_name = data['name']
                country = data['sys']['country']
                temperature = data['main']['temp']
                weather_desc = data['weather'][0]['description']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                weather_info = (f"City: {city_name}, {country}\n"
                                f"Temperature: {temperature}°C\n"
                                f"Weather: {weather_desc}\n"
                                f"Humidity: {humidity}%\n"
                                f"Wind Speed: {wind_speed} m/s")

                weather_label.config(text=weather_info)
            else:
                messagebox.showerror("Error", "City not found!")
                weather_label.config(text="")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")
            weather_label.config(text="")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        weather_label.config(text="")

# Setting up the GUI
root = tk.Tk()
root.title("Weather Dashboard")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=10)

city_label = tk.Label(frame, text="Enter City:", font=("Helvetica", 12))
city_label.grid(row=0, column=0, pady=5)

city_entry = tk.Entry(frame, font=("Helvetica", 12), width=20)
city_entry.grid(row=0, column=1, pady=5)

search_button = tk.Button(frame, text="Search", font=("Helvetica", 12), command=get_weather)
search_button.grid(row=0, column=2, pady=5, padx=10)

weather_label = tk.Label(root, text="", font=("Helvetica", 14), justify="left")
weather_label.pack(pady=20)

root.mainloop()
