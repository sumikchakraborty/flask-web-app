from . import db

class Applicant(db.Model):
    __tablename__ = "applicant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    score = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Applicant {self.name} - {self.score}>"
