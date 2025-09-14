from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    app = Flask(__name__, template_folder=template_dir)

    db_user = os.getenv("POSTGRES_USER", "user")
    db_pass = os.getenv("POSTGRES_PASSWORD", "password")
    db_host = os.getenv("POSTGRES_HOST", "db")
    db_name = os.getenv("POSTGRES_DB", "applicants_db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Auto-create tables
    with app.app_context():
        from .models import Applicant
        db.create_all()

    from .routes import bp
    app.register_blueprint(bp, url_prefix="/api")

    @app.route("/")
    def root_redirect():
        return redirect("/api/")  # simple redirect to the blueprint root

    return app
