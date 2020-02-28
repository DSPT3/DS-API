"""  Main application for Spotify Flask App """
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

DB = SQLAlchemy()

# Make app factory
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spotify_tracks.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    conn = sqlite3.connect('spotify_tracks.sqlite3')

    @app.route("/")
    def root():
        return render_template('base.html', title='Home')
    return app