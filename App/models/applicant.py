from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()

class applicant(db.Model):
    __tablename__ = 'applicants'

    applicantID = db.Column(db.String, primary_key = true)
    name = db.Column(db.String, nullable = False)
    resume = db.Column(db.String, nullable = False)

    def __init__(self, applicantID, name, resume):
        self.applicantID = applicantID
        self.name = name
        self.resume = resume

#This method allows applicants to create job applications
    def applyToJob(self, job):
        from models.applcation import Application
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
        return f'<Applicant {self.name}>'
