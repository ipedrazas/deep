from eve import Eve
from flask.ext.cors import CORS
import json
from flask import request


app = Eve()
cors = CORS(app)


@app.route("/version")
def version():
    return 'Deep API v0.0.2'


@app.route("/debug", methods=['POST'])
def add_link():
    pjson = json.loads(request.data)
    app.logger.debug(pjson)
    return request.data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
