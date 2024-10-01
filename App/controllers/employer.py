from App.models.employer import Employer
from App import db

def create_employer():
    employerID = input('Enter employer ID: ')
    name = input('Enter employer name: ')
    company = input('Enter employer company: ')

    new_emp = Employer(
        employerID = employerID,
        name = name,
        company=company
    )

    db.session.add(new_emp)
    db.session.commit()

    print(f'Employer {name} created successfully')