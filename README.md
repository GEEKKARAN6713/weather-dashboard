# 🌤️ Weather Dashboard App

A modern, clean weather application built with Python and Tkinter that provides real-time weather information for any city worldwide.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🔍 **Smart City Search** - Automatically converts city names to coordinates
- 🌡️ **Real-time Weather Data** - Current temperature, humidity, wind speed, and more
- 🎨 **Modern Dark Theme** - Clean and professional UI design
- 🌍 **No API Keys Required** - Uses free Open-Meteo API
- ⚡ **Fast & Responsive** - Instant weather updates
- 🛡️ **Error Handling** - Graceful handling of network issues and invalid inputs

## 📸 Screenshots

<div align="center">
  <img src="screenshot.png" width="600" alt="Weather Dashboard">
  <p><em>Modern dark-themed weather dashboard displaying real-time data</em></p>
</div>

### Features Visible:
- 🔍 Smart city search with instant results
- 🌡️ Current temperature with "feels like" metric
- 💧 Humidity percentage display
- 💨 Wind speed information
- 🌧️ Precipitation data
- 🎨 Clean, modern dark UI theme

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/GEEKKARAN6713/weather-dashboard.git
cd weather-dashboard
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - **Windows:** `venv\Scripts\activate`
   - **Mac/Linux:** `source venv/bin/activate`

4. Install required packages:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the application:
```bash
python weather_app.py
```

1. Enter any city name in the search box
2. Press Enter or click the "Search" button
3. View real-time weather information!

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Tkinter** - GUI framework
- **Open-Meteo API** - Weather and geocoding data
- **Requests** - HTTP library for API calls

## 📦 Project Structure

```
weather-dashboard/
│
├── weather_app.py       # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
└── screenshot.png      # App screenshot
```

### File Descriptions:

- **weather_app.py** - Contains the main Weather Dashboard application with Tkinter GUI, API integration, and all weather fetching logic
- **requirements.txt** - Lists all Python packages required to run the app (requests library)
- **README.md** - Complete project documentation with installation instructions and usage guide
- **.gitignore** - Specifies which files Git should ignore (virtual environment, cache files, etc.)

## 🌟 Features in Detail

### Weather Information Displayed:
- Current temperature
- "Feels like" temperature
- Humidity percentage
- Wind speed
- Precipitation levels
- Weather condition with emoji icons
- Location details (City, Region, Country)

### Smart City Search:
The app uses Open-Meteo's Geocoding API to:
- Convert city names to precise coordinates
- Handle cities with similar names
- Provide accurate location information

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Karan Kamble**
- GitHub: [@GEEKKARAN6713](https://github.com/GEEKKARAN6713)
- Email: karankamble6713@gmail.com

## 🙏 Acknowledgments

- Weather data provided by [Open-Meteo](https://open-meteo.com/)
- Icons and emojis from Unicode standard
- Built with ❤️ using Python

## 📞 Support

If you encounter any issues or have questions, please:
- Open an issue on GitHub
- Contact me via email

---

⭐ **Star this repository if you find it helpful!**
