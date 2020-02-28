"""  Main application for Spotify Flask App """

from flask import Flask

# Make app factory
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return "Welcome to Build Week Spotify Team!!!"
    return app