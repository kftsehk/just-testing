import os

# Missing packages/import will fail healthcheck
from flask import Flask
app = Flask(__name__)

# TODO: load your models here
# Exception will not pass healthcheck
# raise Exception("Model error")

if os.getenv('CI') != '1':
    # TODO: init anything that requires a connection, these will not run in CI build
    # This exception will pass healthcheck
    raise Exception("Network error")
    pass

@app.route('/healthcheck')
def healthcheck():
    return "OK!"

if __name__ == '__main__':
    # Mounting incorrect port will not pass healthcheck
    # app.run(host='0.0.0.0', port=81)
    app.run(host='0.0.0.0', port=80)