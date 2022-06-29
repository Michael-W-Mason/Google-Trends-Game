# Main file that defines our app in flask_app
from flask import Flask
from flask_cors import CORS

# Creates an instance of our app
app = Flask(__name__, static_url_path="/trendy/static")
CORS(app)

# Used for sessions
app.secret_key = "sd;fioajhndp;aiosudhv[asoduih"