from App.models.job import Job
from App import db

def view_jobs():
    jobs = Job.query.all()
    if jobs:
        for job in jobs:
            print(f'JobID: {job.jobID}, Title: {job.title}, Company: {job.company}, Description: {job.description}, Requirements: {job.requirements}')
    else:
        print('No jobs found.')

def view_job():
    jobID = input('Enter Job ID: ')
    job = Job.query.get(jobID)
    if job:
        print(f'JobID: {job.jobID}, Title: {job.title}, Company: {job.company}, Description: {job.description}, Requirements: {job.requirements}')
    else:
        print('No job found.')

def create_job():
    title = input('Enter new job title: ')
    description = input('Enter Job description: ')
    jRequirements = input('Enter Job requirements: ')
    company = input('Enter the company name: ')
    employerID = input('Enter the employer ID: ')

    new_job = Job(
        title = title,
        description = description,
        requirements = jRequirements,
        company = company,
        employerID = employerID
    )

    db.session.add(new_job)
    db.session.commit()

    print(f'Job {title} created successfully')

def view_job_applicants():
    jobID = input('Enter the JobID: ')
    job = Job.query.get(jobID)
    if job:
        applications = job.applications
        if not applications:
            print(f'No applicants for job {job.title}')
        else:
            for app in applications:
                print(f"Applicant ID: {app.applicantID}, Application ID: {app.applicationID}")
    else:
        print('Job not found.')