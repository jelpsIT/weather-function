﻿# Serverless Weather Fetcher

A serverless Azure Function built with Python that fetches real-time weather data from OpenWeatherMap and logs it to Azure Blob Storage.

## Features
- **Live URL**: [https://jelps-weather-function.azurewebsites.net/api/weather?city=London](https://jelps-weather-function.azurewebsites.net/api/weather?city=London)
- **Technologies**: Azure Functions (Consumption Plan), Python, OpenWeatherMap API, Azure Blob Storage
- **CI/CD**: GitHub Actions for automated deployment
- **Logging**: Weather data saved as JSON blobs in `jelpsweatherstorage/weather-logs`

## Usage
- **Endpoint**: `GET /api/weather?city=<city_name>`
- **Example**: `https://jelps-weather-function.azurewebsites.net/api/weather?city=London`
- **Response**: 
  ```json
  {
    "city": "London",
    "temp": 15.5,
    "description": "clear sky",
    "timestamp": "2025-03-27T18:30:00.123456"
  }

Logs are stored in Blob Storage with filenames like weather_2025-03-27T18-30-00.json.
## Setup
Clone: git clone https://github.com/jelpsIT/weather-function.git
Install dependencies: pip install -r requirements.txt
Deploy to Azure Functions with a storage account (AzureWebJobsStorage).
## Project Highlights
Serverless architecture on Azure’s free tier.
Automated CI/CD pipeline with GitHub Actions.
Integration with Blob Storage for data persistence.
