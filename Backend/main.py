import flask
from flask_socketio import SocketIO, send

app = flask.Flask(__name__)

@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Hello FlaskReact")


app.run(debug=True)