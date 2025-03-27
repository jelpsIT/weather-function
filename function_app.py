import azure.functions as func
import requests
import json
from datetime import datetime

app = func.FunctionApp()

@app.route(route="weather", auth_level=func.AuthLevel.ANONYMOUS)
def get_weather(req: func.HttpRequest) -> func.HttpResponse:
    city = req.params.get('city', 'London')  # Default to London
    api_key = "3e174705e61fc91d949cb4f7ecc29e44" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        result = {
            "city": weather_data["name"],
            "temp": weather_data["main"]["temp"],
            "description": weather_data["weather"][0]["description"],
            "timestamp": datetime.utcnow().isoformat()
        }

        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json",
            status_code=200
        )
    except requests.RequestException as e:
        return func.HttpResponse(f"Error fetching weather: {str(e)}", status_code=500)