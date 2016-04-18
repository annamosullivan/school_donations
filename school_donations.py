from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps


app = Flask(__name__)


MONGODB_HOST = 'ds013260.mlab.com'
MONGODB_PORT = 13260
DBS_NAME = 'heroku_6hq98jg7'
MONGO_URI = 'mongodb://root:root@ds013260.mlab.com:13260/heroku_6hq98jg7'
COLLECTION_NAME = 'opendata_projects_clean'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorsUSA/projects")
def donor_projects():
    connection = MongoClient(MONGO_URI)
    ##collection = connection[DBS_NAME][COLLECTION_NAME]
    ##connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=55000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
