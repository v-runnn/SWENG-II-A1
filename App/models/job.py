from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    __tablename__ = 'jobs'

    jobID = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)
    requirements = db.Column(db.String, nullable=False)

    employerID = db.Column(db.String, db.ForeignKey('employers.employerID'), nullable=False)

    def __repr__(self):
        return f'<Job {self.title} at {self.company}>'