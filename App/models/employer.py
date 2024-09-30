from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class Employer(db.Model):
    __tablename__ = 'employers'

    employerID = db.Column(sb.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)

    jobs = db.relationship('Job', backref='employer', lazy=True)

    def __init__(self, employerID, name,  company):
        self.employerID = employerID,
        self.name = name,
        self.company = company

    def create_job(self, title, description, requirements):
        from models.job import Job
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
        from models.applications import Application
        return Application.query.filter_by(jobID=jobID).all()

    def __repr__ (self):
        return f'<Employer {self.name} from {self.company}>'
