import os

from flask import Flask
app = Flask(__name__)

# load your models here

if os.environ['CI']!=='1':
    # init anything that requires a connection, these will not be checked
    pass

@app.route('/')
def healthcheck():
    return "OK!"

if __name__ == '__main__':
    app.run()