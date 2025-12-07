import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime
import json

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Dashboard")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Dark theme colors
        self.bg_color = "#1a1a2e"
        self.secondary_bg = "#16213e"
        self.accent_color = "#0f3460"
        self.text_color = "#eaeaea"
        self.highlight_color = "#e94560"
        
        self.root.configure(bg=self.bg_color)
        self.create_ui()
        
    def create_ui(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg=self.secondary_bg, height=80)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="☁ Weather Dashboard",
            font=("Helvetica", 24, "bold"),
            bg=self.secondary_bg,
            fg=self.text_color
        )
        title_label.pack(pady=20)
        
        # Search Frame
        search_frame = tk.Frame(self.root, bg=self.bg_color)
        search_frame.pack(fill="x", padx=20, pady=10)
        
        search_label = tk.Label(
            search_frame,
            text="Enter City Name:",
            font=("Helvetica", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        search_label.pack(anchor="w", pady=(0, 5))
        
        # Search entry with button frame
        entry_frame = tk.Frame(search_frame, bg=self.bg_color)
        entry_frame.pack(fill="x")
        
        self.city_entry = tk.Entry(
            entry_frame,
            font=("Helvetica", 14),
            bg=self.secondary_bg,
            fg=self.text_color,
            insertbackground=self.text_color,
            relief="flat",
            bd=0
        )
        self.city_entry.pack(side="left", fill="x", expand=True, ipady=10, ipadx=10)
        self.city_entry.bind("<Return>", lambda e: self.fetch_weather())
        
        search_btn = tk.Button(
            entry_frame,
            text="Search",
            font=("Helvetica", 12, "bold"),
            bg=self.highlight_color,
            fg=self.text_color,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.fetch_weather,
            padx=20
        )
        search_btn.pack(side="left", padx=(10, 0), ipady=8)
        
        # Weather Display Frame
        self.weather_frame = tk.Frame(self.root, bg=self.accent_color)
        self.weather_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Initial message
        self.create_welcome_message()
        
    def create_welcome_message(self):
        welcome_label = tk.Label(
            self.weather_frame,
            text="🌍\n\nSearch for a city to view\nweather information",
            font=("Helvetica", 16),
            bg=self.accent_color,
            fg=self.text_color,
            justify="center"
        )
        welcome_label.place(relx=0.5, rely=0.5, anchor="center")
        
    def get_coordinates(self, city_name):
        """Convert city name to coordinates using Open-Meteo Geocoding API"""
        try:
            geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
            params = {
                "name": city_name,
                "count": 1,
                "language": "en",
                "format": "json"
            }
            
            response = requests.get(geocoding_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if "results" not in data or len(data["results"]) == 0:
                return None
                
            result = data["results"][0]
            return {
                "latitude": result["latitude"],
                "longitude": result["longitude"],
                "name": result["name"],
                "country": result.get("country", ""),
                "admin1": result.get("admin1", "")
            }
            
        except requests.exceptions.Timeout:
            messagebox.showerror("Error", "Request timed out. Please check your internet connection.")
            return None
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Network error: {str(e)}")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")
            return None
    
    def get_weather(self, latitude, longitude):
        """Fetch weather data using Open-Meteo Weather API"""
        try:
            weather_url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m,wind_direction_10m",
                "timezone": "auto"
            }
            
            response = requests.get(weather_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.Timeout:
            messagebox.showerror("Error", "Request timed out. Please try again.")
            return None
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")
            return None
    
    def get_weather_description(self, code):
        """Convert weather code to description"""
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Foggy",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with hail",
            99: "Thunderstorm with hail"
        }
        return weather_codes.get(code, "Unknown")
    
    def get_weather_emoji(self, code):
        """Get emoji based on weather code"""
        if code == 0:
            return "☀️"
        elif code in [1, 2]:
            return "🌤️"
        elif code == 3:
            return "☁️"
        elif code in [45, 48]:
            return "🌫️"
        elif code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
            return "🌧️"
        elif code in [71, 73, 75, 77, 85, 86]:
            return "❄️"
        elif code in [95, 96, 99]:
            return "⛈️"
        return "🌡️"
    
    def fetch_weather(self):
        city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name")
            return
        
        # Clear previous weather display
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        # Show loading message
        loading_label = tk.Label(
            self.weather_frame,
            text="Loading...",
            font=("Helvetica", 14),
            bg=self.accent_color,
            fg=self.text_color
        )
        loading_label.place(relx=0.5, rely=0.5, anchor="center")
        self.root.update()
        
        # Get coordinates
        location = self.get_coordinates(city)
        
        if not location:
            loading_label.destroy()
            error_label = tk.Label(
                self.weather_frame,
                text=f"City '{city}' not found.\nPlease check the spelling and try again.",
                font=("Helvetica", 14),
                bg=self.accent_color,
                fg=self.highlight_color,
                justify="center"
            )
            error_label.place(relx=0.5, rely=0.5, anchor="center")
            return
        
        # Get weather data
        weather_data = self.get_weather(location["latitude"], location["longitude"])
        
        if not weather_data:
            loading_label.destroy()
            return
        
        # Display weather
        loading_label.destroy()
        self.display_weather(location, weather_data)
    
    def display_weather(self, location, weather_data):
        """Display weather information in the UI"""
        current = weather_data["current"]
        
        # Location label
        location_text = f"{location['name']}, {location['country']}"
        if location['admin1']:
            location_text = f"{location['name']}, {location['admin1']}, {location['country']}"
        
        location_label = tk.Label(
            self.weather_frame,
            text=location_text,
            font=("Helvetica", 20, "bold"),
            bg=self.accent_color,
            fg=self.text_color
        )
        location_label.pack(pady=(30, 10))
        
        # Weather emoji
        weather_code = current.get("weather_code", 0)
        emoji = self.get_weather_emoji(weather_code)
        
        emoji_label = tk.Label(
            self.weather_frame,
            text=emoji,
            font=("Helvetica", 60),
            bg=self.accent_color
        )
        emoji_label.pack(pady=10)
        
        # Temperature
        temp = current.get("temperature_2m", "N/A")
        temp_label = tk.Label(
            self.weather_frame,
            text=f"{temp}°C",
            font=("Helvetica", 48, "bold"),
            bg=self.accent_color,
            fg=self.text_color
        )
        temp_label.pack()
        
        # Weather description
        description = self.get_weather_description(weather_code)
        desc_label = tk.Label(
            self.weather_frame,
            text=description,
            font=("Helvetica", 16),
            bg=self.accent_color,
            fg=self.text_color
        )
        desc_label.pack(pady=(5, 20))
        
        # Details frame
        details_frame = tk.Frame(self.weather_frame, bg=self.secondary_bg)
        details_frame.pack(fill="x", padx=30, pady=10)
        
        # Create grid of weather details
        details = [
            ("Feels Like", f"{current.get('apparent_temperature', 'N/A')}°C"),
            ("Humidity", f"{current.get('relative_humidity_2m', 'N/A')}%"),
            ("Wind Speed", f"{current.get('wind_speed_10m', 'N/A')} km/h"),
            ("Precipitation", f"{current.get('precipitation', 'N/A')} mm")
        ]
        
        for i, (label, value) in enumerate(details):
            row = i // 2
            col = i % 2
            
            detail_frame = tk.Frame(details_frame, bg=self.secondary_bg)
            detail_frame.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            
            tk.Label(
                detail_frame,
                text=label,
                font=("Helvetica", 10),
                bg=self.secondary_bg,
                fg="#888888"
            ).pack()
            
            tk.Label(
                detail_frame,
                text=value,
                font=("Helvetica", 14, "bold"),
                bg=self.secondary_bg,
                fg=self.text_color
            ).pack()
        
        details_frame.grid_columnconfigure(0, weight=1)
        details_frame.grid_columnconfigure(1, weight=1)
        
        # Last updated
        now = datetime.now().strftime("%I:%M %p")
        update_label = tk.Label(
            self.weather_frame,
            text=f"Last updated: {now}",
            font=("Helvetica", 10),
            bg=self.accent_color,
            fg="#888888"
        )
        update_label.pack(side="bottom", pady=20)

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()