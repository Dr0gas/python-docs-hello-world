from flask import Flask
app = Flask(__name__)

@app.route("/d0ug.html")
def hello():
    return "U3ViZG9tYWluIFRha2VvdmVyIGJ5OmQwdWcK"
