import json
import os

from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/api/list", methods=['GET'])
def list():
    with open(f'{os.path.dirname(__file__)}/data.json', encoding='utf-8') as json_file:
        json_data = json.loads(json_file.read())
    return jsonify(json_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
