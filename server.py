# Main file that runs the entire app

# Imports our app with secret key
from flask_app import app

# Imports our routing to the app
from flask_app.controllers import games

# Make sure we run this script not as a module
if __name__ == "__main__":
    # gameloop.start_game()
    app.run(debug=True, host='127.0.0.1')