# sqlalchemy-challenge
# Overview
This project provides a Flask API to access and analyze climate data for Hawaii. The API allows users to retrieve precipitation and temperature data for various stations across the state.

# Features
Retrieve precipitation data for the last year
Get a list of all station names
Retrieve temperature data for the last year
Retrieve temperature data from a specified start date
Retrieve temperature data between a specified start and end date
API Endpoints
Precipitation Data
/api/v1.0/precipitation: Returns precipitation data for the last year
Station List
/api/v1.0/stations: Returns a list of all station names
Temperature Data
/api/v1.0/tobs: Returns temperature data for the last year
/api/v1.0/<start>: Returns temperature data from a specified start date
/api/v1.0/<start>/<end>: Returns temperature data between a specified start and end date
Usage
To use the API, simply send a GET request to the desired endpoint. For example, to retrieve precipitation data, send a GET request to http://localhost:5000/api/v1.0/precipitation.

# Requirements
Python 3.x
Flask
SQLAlchemy
Pandas
Matplotlib (optional for data visualization)
Installation
Clone the repository: git clone https://github.com/your-username/hawaii-climate-api.git
Install the required packages: pip install -r requirements.txt
Run the API: python app.py
