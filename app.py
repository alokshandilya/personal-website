from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
uri = os.getenv("mongo_uri")

# Create a new client and connect to the server
client= MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Access the database and collection
db = client.portfolio
projects_collection = db.projects

# Create a Flask application
app = Flask(__name__)

@app.route("/")
def index():
    # Retrieve all documents from the 'projects' collection
    projects = list(projects_collection.find())
    return render_template("home.html", projects=projects)

# TODO: later
# @app.route("/api/projects")
# def list_projects():
#     return jsonify(projects_collection)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
