#dependencies
from flask import Flask, jsonify

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#Database Setup

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)



# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station





#Flask Setup
app = Flask(__name__)


#Flask Routes

@app.route("/api/v1.0/precipitation")
def weather_data():

    return jsonify(#WeatherDataDict)
    
#homepage

@app.route("/")
def welcome():
    return(
        f"Welcome to the Surfs Up Climate Analysis API <br/>"
        f"Available Routes: <br/>"
        f"Station List: /api/v1.0/stations <br/>"
        f"Precipitation Data: /api/v1.0/precipitation <br/>"
        f"Tempature Data: /api/v1.0/tobs <br/>"
        #need to add the start and end)
        
@app.route("/api/v1.0/stations")
    def stations():
        # Create our session (link) from Python to the DB
        session = Session(engine)
        
        #return a list of all the stations 
        
        results = session.query(Station.name, ).all()
        
        session.close()
        #convert into a list
        all_stations = lst(np.ravel(results))
        
        return jsonify (all_stations)
