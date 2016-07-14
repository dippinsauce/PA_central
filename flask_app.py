
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="dippinsauce",
    password="jyrqskrM1D9M2NAu0atF",
    hostname="dippinsauce.mysql.pythonanywhere-services.com",
    databasename="dippinsauce$default",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db=SQLAlchemy(app)

class lake_interior_temp(db.Model):
    __tablename__ = "lake_interior_temp"

    id = db.Column(db.Integer, primary_key=True)
    post_time = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)

class home_server_status(db.Model):
    __tablename__ = "home_server_status"

    id = db.Column(db.Integer, primary_key=True)
    post_time = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)


class test_post(db.Model):
    __tablename__ = "test"

    id = db.Column(db.Integer, primary_key=True)
    post_time = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    test1 = db.Column(db.Float)
    test2 = db.Column(db.Integer)

comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)
    comments.append(request.form["contents"])
    return redirect(url_for('index'))

#Start the restful API routes
@app.route('/dbase/lake/interior_temp/<rawdata>', methods=["GET", "POST"])
def putLakeInteriorTemps(rawdata):
    ret_string = 'got your data, it looks like this: ' + str(rawdata)
    return ret_string

#Home applications
@app.route('/home/server_status/<rawdata>', methods=["POST"])
def putServerInfo(rawdata):
    ret_string = 'got your data, it looks like this: ' + str(rawdata)
    return ret_string

@app.route('/wibble/')
def wibble():
    return 'nothing interesting here'
