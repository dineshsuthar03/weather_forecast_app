# ⛅ Weather Forecast App

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Site-blue)](https://weather-forecast-app-v1.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.12+-yellow?logo=python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-Latest-green?logo=django)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-purple)](LICENSE.md)

A modern, responsive Weather Forecast application built with Django and OpenWeatherMap API. Get real-time weather updates including temperature, humidity, wind speed, and more with a beautiful, user-friendly interface.

![Weather App Screenshot](https://raw.githubusercontent.com/yourusername/weather-forecast-app/main/screenshot.png)

🔗 **Live Demo:** [Weather Forecast App](https://weather-forecast-app-v1.onrender.com)

## ✨ Features

- 🔍 Instant weather search by city name
- 🌡️ Real-time weather data display:
  - Current temperature and "feels like" temperature
  - Humidity and wind speed
  - Cloud coverage and visibility
  - Sunrise and sunset times (UTC)
- 🎨 Modern, responsive interface
- 📱 Mobile-friendly design
- ⚡ Fast and reliable updates
- 🌐 Global city coverage

## 🛠️ Tech Stack

- **Backend:** Django 4.2+
- **API:** OpenWeatherMap API
- **Frontend:** 
  - HTML5
  - CSS3 (Responsive Design)
  - Font Awesome Icons
- **Deployment:** Gunicorn + Render
- **Environment:** Python 3.12+

## 📋 Prerequisites

Before starting, make sure you have:

- Python 3.12 or higher
- Git
- A code editor (VSCode, PyCharm, etc.)
- An OpenWeatherMap API key ([Get here](https://openweathermap.org/api))

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/weather-forecast-app.git
   cd weather-forecast-app
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate it
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   ```bash
   # Create .env file in root directory
   echo "OPENWEATHERMAP_API_KEY=your_api_key_here" > .env
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the App**
   - Open your browser and go to `http://127.0.0.1:8000`

## 🌐 API Integration

The app uses OpenWeatherMap's Current Weather Data API:

```python
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
PARAMS = {
    "q": city_name,
    "appid": API_KEY,
    "units": "metric"
}
```

Example Response:
```json
{
  "coord": {"lon": 72.85, "lat": 19.01},
  "weather": [
    {
      "description": "few clouds",
      "icon": "02d"
    }
  ],
  "main": {
    "temp": 302.94,
    "feels_like": 303.75,
    "humidity": 49
  }
}
```

## 🚀 Deployment

### Deploying to Render

1. Create a Render account
2. Connect your GitHub repository
3. Configure build settings:
   ```bash
   # Build command
   pip install -r requirements.txt

   # Start command
   gunicorn weather_project.wsgi:application
   ```
4. Add environment variables:
   - `OPENWEATHERMAP_API_KEY`
   - `DJANGO_SECRET_KEY`
   - `DEBUG=False`

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE.md` for more information.

## 👤 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

## 🌟 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for the weather data API
- [Font Awesome](https://fontawesome.com/) for the icons
- [Django](https://www.djangoproject.com/) for the amazing framework

---
⭐ Star this repository if you find it helpful!