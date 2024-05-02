from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
    {
        "id": 1,
        "title": "Movie Rating Review Application",
        "description": "A web application to rate and review movies, lacks a dedicated database, uses local storage to store data.",
        "domain": "Web Development",
        "tech-stack": "HTML, CSS, TypeScript, Angular",
    },
    {
        "id": 2,
        "title": "Bengali and Assamese Handwritten Character Recognition",
        "description": "A machine learning model to recognize handwritten Bengali and Assamese characters and find similarities between them.",
        "domain": "Machine Learning",
        "tech-stack": "Python, Tensorflow, Keras",
    },
    {
        "id": 3,
        "title": "Personal Portfolio Website",
        "description": "Personal portfolio website to showcase projects and skills.",
        "domain": "Web Development",
        "tech-stack": "Python, Flask",
    },
]


@app.route("/")
def hello_world():
    return render_template("home.html", projects=PROJECTS)


@app.route("/api/projects")
def list_projects():
    return jsonify(PROJECTS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
