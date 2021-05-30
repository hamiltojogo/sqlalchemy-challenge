import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from dateutil.relativedelta import relativedelta
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# Save reference to the table
Measurement = Base.classes.measurement

Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"for temp max, temp min, and average temp since a give date (enter as YYYY-M-D):  /api/v1.0/<start><br/>"
        f"for temp max, temp min, and average temp between two given dates (enter as YYYY-M-D/YYYY-M-D):   /api/v1.0/<start>/<end>"

    )
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    results = session.query(Station.name).all()

    session.close()

    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/precipitation")
def precipitation ():
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    precip_data = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict['date']= date
        precip_dict['prcp'] = prcp
        precip_data.append(precip_dict)

    return jsonify(precip_data)

@app.route("/api/v1.0/tobs")
def tobs ():
    session = Session(engine)

    last_date = dt.datetime(2017, 8, 23)
    year_before = last_date - relativedelta(months=+12)

    active_station = 'USC00519281'

    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.station == active_station).filter(Measurement.date >= year_before).all()

    session.close()

    tobs_data = list(np.ravel(results))

    return jsonify(tobs_data)

@app.route("/api/v1.0/<start>") #need to change the string into three elements in a list because dt wants three int arguments. 
def tobs_start(start):
    session = Session(engine)


    year, month, day = start.split("-")

    year = int(year)
    month = int(month)
    day = int(day)
        
    start_date = dt.datetime(year, month, day)


    sel = [
        func.max(Measurement.tobs),
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        Measurement.date
    ]
    results = session.query(*sel).filter(Measurement.date >= start_date).all()

    session.close()

    start_tobs= list(np.ravel(results))

    return jsonify(start_tobs)


@app.route("/api/v1.0/<start>/<end>")
def start_end (start,end):
    session = Session(engine)

    #format start date string into int
    start_year, start_month, start_day = start.split("-")

    start_year = int(start_year)
    start_month = int(start_month)
    start_day = int(start_day)


    start_date = dt.datetime(start_year, start_month, start_day)

    #format end date string into int
    end_year, end_month, end_day = end.split("-")

    end_year = int(end_year)
    end_month = int(end_month)
    end_day = int(end_day)

    end_date = dt.datetime(end_year, end_month, end_day)

    sel = [
        func.max(Measurement.tobs),
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        Measurement.date
    ]
    results = session.query(*sel).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    start_end_tobs = list(np.ravel(results))

    return jsonify(start_end_tobs)

if __name__ == '__main__':
    app.run(debug = True)
