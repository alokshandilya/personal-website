from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for,
    make_response,
)
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import json
from bson import ObjectId
import os

# Load environment variables
load_dotenv()
uri = os.getenv("mongo_uri")
username = os.getenv("username")
password = os.getenv("password")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Access the database and collection
db = client.portfolio
projects_collection = db.projects

# Create a Flask application
app = Flask(__name__)
auth = HTTPBasicAuth()

# User data
users = {username: generate_password_hash(password)}


@app.route("/")
def index():
    # Retrieve all documents from the 'projects' collection each time the route is accessed
    projects = list(projects_collection.find())
    return render_template("home.html", projects=projects)


@app.route("/google721ed54125969664.html")
def google_verification():
    return render_template("google721ed54125969664.html")


@app.route("/resume")
def get_resume():
    return redirect("https://bit.ly/alokshandilya")


# Helper function to convert MongoDB documents to JSON serializable format
def convert_mongo_document(doc):
    doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
    return doc


# Basic Auth verification callback
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route("/api/projects", methods=["GET"])
def edit_projects():
    # Retrieve all documents from the 'projects' collection each time the route is accessed
    projects = list(projects_collection.find())
    json_data = json.dumps(
        [convert_mongo_document(project) for project in projects], indent=4
    )
    response = make_response(render_template("edit_projects.html", json_data=json_data))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.route("/api/projects", methods=["POST"])
@auth.login_required
def save_projects():
    try:
        # Get the JSON data from form
        json_data = request.form["json_data"]
        new_data = json.loads(json_data)

        # Clear the collection and insert new data
        projects_collection.delete_many({})
        projects_collection.insert_many(new_data)

        return redirect(url_for("edit_projects"))
    except Exception as e:
        return str(e), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
