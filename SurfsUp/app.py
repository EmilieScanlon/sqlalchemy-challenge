import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session.commit()  # Add this line
    results = session.query(Measurement.date, Measurement.prcp).all()
    all_precipitation = []
    for result in results:
        precipitation_dict = {}
        precipitation_dict["date"] = result[0]
        precipitation_dict["prcp"] = result[1]
        all_precipitation.append(precipitation_dict)
    return jsonify(all_precipitation)


@app.route("/api/v1.0/stations")
def stations():
    session.commit()  # Add this line
    results = session.query(Station.station).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    with Session() as session:
        recent_date = session.query(func.max(Measurement.date)).scalar()
        if recent_date is None:
            return jsonify({"error": "No dates found in the database"}), 404
        one_year_ago = recent_date - pd.DateOffset(years=1)
        results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date >= one_year_ago).all()
        all_tobs = []
        for result in results:
            tobs_dict = {}
            tobs_dict["date"] = result[0]
            tobs_dict["tobs"] = result[1]
            all_tobs.append(tobs_dict)
    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def start(start):
    session.commit()  # Add this line
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    start_tobs = list(np.ravel(results))
    return jsonify(start_tobs)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session.commit()  # Add this line
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    start_end_tobs = list(np.ravel(results))
    return jsonify(start_end_tobs)


if __name__ == "__main__":
    app.run(debug=True)