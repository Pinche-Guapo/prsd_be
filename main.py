import flask
flask.Flask

app = flask.Flask(__name__)

@app.route("/layla")

def churu():
    return "tuna churu"

app.run()