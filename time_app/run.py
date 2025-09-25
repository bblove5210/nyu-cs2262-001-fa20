from flask import Flask
app = Flask(__name__)

from datetime import datetime

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    return {'time': datetime.now().strftime("%H:%M:%S")}


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
