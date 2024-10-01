import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.controllers.Application import view_applications_by_job, view_applications_by_applicant
from App.controllers.applicant import view_applicants, view_applicant, create_applicant
from App.controllers.employer import create_employer
from App.controllers.job import view_jobs, view_job, create_job
from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

app.cli.add_command(test)

@app.cli.command("view_applications_by_job", help="Views the applications for a particular job")
def view_R_J():
    view_applications_by_job()
    
@app.cli.command("view_applications_by_applicant", help="Views the applications for a particular applicant")
def view_R_A():
    view_applications_by_applicant()


@app.cli.command("view_applcants", help="Views all the applicants for jobs")
def view_appls():
    view_applicants()

@app.cli.command("view_applcant", help="Views an applicant in the system")
def view_appl():
    view_applicant()

@app.cli.command("apply_to_job", help="Allows a user to apply for jobs")
def apply_to_job():
    apply_to_job()

@app.cli.command("create_applicant", help="Creates applicants")
def create_appl():
    create_applicant()

@app.cli.command("view_jobs", help="Views all the jobs")
def view_jbs():
    view_jobs()

@app.cli.command("view_job", help="Views a job")
def view_jb():
    view_job()

@app.cli.command("create_job", help="Views all the applicants for jobs")
def create_jb():
    create_job()

@app.cli.command("create_employer", help="Creates an employer")
def create_emp():
    create_employer()