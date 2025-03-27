import azure.functions as func
import requests
import json
from datetime import datetime
from azure.storage.blob import BlobServiceClient

app = func.FunctionApp()

@app.route(route="weather", auth_level=func.AuthLevel.ANONYMOUS)
def get_weather(req: func.HttpRequest) -> func.HttpResponse:
    city = req.params.get('city', 'London')
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

        # Log to Blob Storage
        connection_string = req.app.settings["AzureWebJobsStorage"]
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_name = "weather-logs"
        blob_name = f"weather_{result['timestamp'].replace(':', '-')}.json"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(json.dumps(result), overwrite=True)

        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json",
            status_code=200
        )
    except requests.RequestException as e:
        return func.HttpResponse(f"Error fetching weather: {str(e)}", status_code=500)