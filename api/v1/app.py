#!/usr/bin/python3
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

"""cors = CORS(app, resources={r'/*': {'origins': '0.0.0.0'}})"""

@app.teardown_appcontext
def show_tear(execute):
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=getenv('HBNB_API_PORT', 5000),
            threaded=True, debug=True)
