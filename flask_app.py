
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import time
from re import search

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
    unix_post_time = db.Column(db.DateTime) #mysql timestamp field, defaults to current time.
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)

class home_server_status(db.Model):
    __tablename__ = "home_server_status"

    id = db.Column(db.Integer, primary_key=True)
    unix_post_time = db.Column(db.DateTime) #mysql timestamp field, defaults to current time.
    temperature = db.Column(db.Float)
    load_avg = db.Column(db.Float)


class test_post(db.Model):
    __tablename__ = "test"

    id = db.Column(db.Integer, primary_key=True)
    unix_post_time = db.Column(db.DateTime) #mysql timestamp field, defaults to current time.
    test1 = db.Column(db.Float)
    test2 = db.Column(db.Integer)

    def __repr__(self):
        return "<test_post(test1='%s', test2='%s')>" % (
             self.test1, self.test2)

@app.route("/", methods=["GET", "POST"])
def index():

    return render_template('main_page.html')

#Start the restful API routes
##################################
#Lake applications
@app.route('/dbase/lake/interior_temp/<rawdata>', methods=["GET", "POST"])
def putLakeInteriorTemps(rawdata):
    ret_string = 'got your data, it looks like this: ' + str(rawdata)
    return ret_string

#Home applications
@app.route('/home/<rawstring>', methods=["GET"])
def putHomeInfo(rawstring):
    #rawdata example "home_server_status!=0.02@=28.2
    #server_status shows what table....
    get_table = search(r'\S+!', rawstring)
    destination_table = get_table.group(0)
    destination_table = destination_table[:-1]

    #home_server_status
    if destination_table == "home_server_status":
        loadavg_search = search(r'!=\d+.\d+', rawstring)
        loadavg_string = loadavg_search.group(0)
        loadavg_string = loadavg_string[2:]

        temperature_search = search(r'@=\d+.\d+', rawstring)
        temperature_string = temperature_search.group(0)
        temperature_string = temperature_string[2:]

        ret_string = "temp=" + temperature_string + " == load_avg=" + loadavg_string

        try:
            Record = home_server_status(temperature = float(temperature_string), load_avg = float(loadavg_string))
            db.session.add(Record)
            db.session.commit()
            ret_string += ' -- ACKNOWLEDGED --'
            return ret_string
        except:
            ret_string += ' -- Database Failure --'
            return ret_string

    else:
        return "Unrecognized"

@app.route('/test/<rawstring>')
def test(rawstring):
    # incoming string construction
    # !=xxx@=yyy  <> Where xxx is test1 and yyy is test2
    # Total String 'http://dippinsauce.pythonanywhere.com/test/!=x.xx@=yy.y'

    #new_record = test_post()
    t1 = search(r'!=\d+.\d+', rawstring)
    t1a = t1.group(0)
    t1a = t1a[2:]

    ret_string = 'got your data, it looks like this: ' + str(rawstring)
    ret_string += '\n'
    ret_string += 't1=' + t1a

    t2 = search(r'@=\d+', rawstring)
    t2a = t2.group(0)
    t2a = t2a[2:]

    ret_string += '\n'
    ret_string += 't2=' + t2a

    t1a = float(t1a)
    t2a = int(t2a)
    try:
        Record = test_post(test1 = t1a, test2 = t2a)
        db.session.add(Record)
        db.session.commit()
    except:
        return "Database problem"


    return ret_string
