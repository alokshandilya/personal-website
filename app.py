from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
uri = os.getenv("mongo_uri")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Access the database and collection
db = client.portfolio
projects_collection = db.projects

# Create a Flask application
app = Flask(__name__)


# Retrieve all documents from the 'projects' collection
projects = list(projects_collection.find())


@app.route("/")
def index():
    return render_template("home.html", projects=projects)


# Helper function to convert MongoDB documents to JSON serializable format
def convert_mongo_document(doc):
    doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
    return doc


@app.route("/api/projects")
def list_projects():
    json_data = [convert_mongo_document(project) for project in projects]
    return jsonify(json_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
