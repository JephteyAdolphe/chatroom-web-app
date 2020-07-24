import flask
from flask_socketio import SocketIO, send

app = flask.Flask(__name__)
app.config['SECRET KEY'] = 'mysecret'
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
    #return flask.render_template("index.html", token="Hello Flask")


if __name__ == '__main__':
    socketio.run(app)
    flask.render_template("index.html", token="Hello Flask")
