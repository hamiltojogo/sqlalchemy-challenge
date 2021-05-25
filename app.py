#dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import datetime as dt

#Weather Data Dict



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
        
