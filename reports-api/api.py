from eve import Eve
from flask.ext.cors import CORS
import json
from flask import request
# import StringIO
from xml2json import xml_to_json


def before_insert(resource_name, items):
    for item in items:
        item['report'] = xml_to_json(item['report'])
        print str(item)

app = Eve()
cors = CORS(app)

app.on_insert += before_insert


@app.route("/version")
def version():
    return 'Deep Rerports API v0.0.1'


@app.route("/debug", methods=['POST'])
def add_link():
    pjson = json.loads(request.data)
    app.logger.debug(pjson)
    return request.data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
