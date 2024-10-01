from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Application(db.Model):
    __tablename__ = 'applications'

    applicationID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.Boolean, nullable=False, default=True)
    dateApplied = db.Column(db.DateTime, default=datetime.utcnow)

    applicantID = db.Column(db.String, db.ForeignKey('jobs.jobID'), nullable=False)
    jobID = db.Column(db.String, db.ForeignKey('jobs.jobID'), nullable=False)

    def __repr__(self):
        return f'<Application {self.applicationID} by Applicant {self.applicantID} for Job {self.jobID}>'