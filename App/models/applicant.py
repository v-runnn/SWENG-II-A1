from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from App.models.application import Application

db=SQLAlchemy()

class Applicant(db.Model):
    __tablename__ = 'applicants'

    applicantID = db.Column(db.String, primary_key = True)
    name = db.Column(db.String, nullable = False)
    resume = db.Column(db.String, nullable = False)

    def __init__(self, applicantID, name, resume):
        self.applicantID = applicantID
        self.name = name
        self.resume = resume

    #This method allows applicants to create job applications
    def applyToJob(self, job):
        application = Application(
            status = True,
            dateApplied = datetime.now(),
            applicantID = self.applicantID,
            jobID = job.jobID
        )
        db.session.add(application)
        db.session.commit()
        return application

    def __repr__(self):
        return f'<Applicant {self.name}> '
