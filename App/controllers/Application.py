from App.models.application import Application

def view_applications_by_job():
    jobID = input('Enter the job ID: ')
    applications = Application.query.filter_by(jobID=jobID).all()
    if applications:
        for app in applications:
            if app.status:
                print(f'Application ID: {app.applicationID}, Applicant ID: {app.applicantID}, Status: Active, Date Applied: {app.dateApplied}')
            else:
                print(f'Application ID: {app.applicationID}, Applicant ID: {app.applicantID}, Status: Inactive, Date Applied: {app.dateApplied}')
    else:
        print('No applicants found for this job.')

def view_applications_by_applicant():
    applicantID = input('Enter the applicant ID: ')
    applications = Application.query.filter_by(applicantID = applicantID).all()
    if applications:
        for app in applications:
            if app.status:
                print(f'Application ID: {app.applicationID}, Job ID: {app.jobID}, Status: Active, Date Applied: {app.dateApplied}')
            else:
                print(f'Application ID: {app.applicationID}, Job ID: {app.jobID}, Status: Inactive, Date Applied: {app.dateApplied}')
    else:
        print('No applications found for this applicant.')