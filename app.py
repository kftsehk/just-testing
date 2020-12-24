import os

from flask import Flask
app = Flask(__name__)

# load your models here

if os.getenv('CI') != '1':
    # init anything that requires a connection, these will not be checked
    pass

@app.route('/healthcheck')
def healthcheck():
    return "OK!1"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)