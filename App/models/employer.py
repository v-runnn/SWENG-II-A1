from flask_sqlalchemy import SQLAlchemy
from App.models.application import Application
from App.models.job import Job

db = SQLAlchemy()

class Employer(db.Model):
    __tablename__ = 'employers'

    employerID = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)

    def __init__(self, employerID, name,  company):
        self.employerID = employerID,
        self.name = name,
        self.company = company

    def create_job(self, title, description, requirements):

        job = Job(
            title=title,
            description=description,
            requirements=requirements,
            company=self.company,
            employerID=self.employerID
        )
        db.session.add(job)
        db.session.commit()
        return job

    def view_applicants(self, jobID):

        return Application.query.filter_by(jobID=jobID).all()

    def __repr__ (self):
        return f'<Employer {self.name} from {self.company}>'
