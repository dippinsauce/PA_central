
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="dippinsauce",
    password="jyrqskrM1D9M2NAu0atF",
    hostname="dippinsauce.mysql.pythonanywhere-services.com",
    databasename="dippinsauce$lake",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

@app.route("/")
def index():
    return render_template("main_page.html")

#Start the restful API routes
@app.route('/dbase/')
def put_database():
    return 'getting started with dbase rest api'

@app.route('/wibble/')
def wibble():
    return 'nothing interesting here'
