from flask import Blueprint, request, jsonify, render_template
from .models import Applicant
from . import db

bp = Blueprint("app", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/add", methods=["POST"])
def add_applicant():
    data = request.form
    applicant = Applicant(
        name=data.get("name"),
        email=data.get("email"),
        score=float(data.get("score"))
    )
    db.session.add(applicant)
    db.session.commit()
    return "Applicant added!", 200

@bp.route("/applicants/top")
def get_top_applicants():
    applicants = Applicant.query.filter(Applicant.score > 80).all()
    return jsonify([{"name": a.name, "email": a.email, "score": a.score} for a in applicants])
