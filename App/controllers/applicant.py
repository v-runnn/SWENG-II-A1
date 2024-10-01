from App.models.applicant import Applicant
from App.models.application import Application
from App.models.job import Job
from App import db

def view_applicants():
    applicants = Applicant.query.all()
    if applicants:
        for applicant in applicants:
            print(f'ID: {applicant.applicantID}, Name: {applicant.name}, Resume: {applicant.resume}')
    else:
        print('No applicants found.')

def view_applicant():
    applicantID = input('Enter the ID of an applicant to view their applications: ')
    applicant = Application.query.get(applicantID)
    if applicant:
        print(f'ID: {applicant.applicantID}, Name: {applicant.name}, Resume: {applicant.resume}')
    else:
        print('Applicant not found.')

def apply_to_job():
    applicantID = input("Enter your applicant ID: ")
    jobID = input("Enter the job ID of the Job you wish to apply for: ")
    applicant = Applicant.query.get(applicantID)
    job = Job.query.get(jobID)

    if applicant and job:
        applicant.apply_to_job(job)
        print(f'{applicant.name} successfully applied to {job.title}')
    elif not applicant:
        print('Applicant not found.')
    else:
        print('Job not found.')

def create_applicant():
    applicantID = input('Enter a new applicant ID: ')
    name = input('Enter your name: ')
    resume = input('Enter your resume: ')

    new_applicant = Applicant(applicantID=applicantID, name=name, resume=resume)
    db.session.add(new_applicant)
    db.session.commit()

    print(f"Applicant {name} created successfully.")