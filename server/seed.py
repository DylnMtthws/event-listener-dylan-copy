#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
from models import Account, Opportunity, Registration, db
from datetime import datetime, timedelta


# Remote library imports
from faker import Faker

# Local imports
from app import app

fake = Faker()

def create_accounts():
    accounts = []
    ROLES= ['Admin', 'User']
    for _ in range(30):
        a = Account(
            username= fake.first_name(),
            password_hash='testpassword',
            name= fake.name(),
            email=fake.email(),
            role= rc(ROLES)    
        )
        accounts.append(a)
    return accounts

# # Create a new opportunity
def create_opportunities():
    opportunities = []
    for _ in range(10):
        o = Opportunity(
            title= fake.sentence(3),
            description = fake.sentence(30),
            start_date = datetime.now(),
            end_date = datetime.now(),
                
        )
        opportunities.append(o)
    return opportunities


def create_registration():
    registrations = []
    for _ in range(10):
        o = Registration(
            registration_date = datetime.now(),
            account_id = randint(1,30),
            opportunity_id = randint(1,10),
        )
        registrations.append(o)
    return registrations
# opportunity1 = Opportunity(
#    title='Test Opportunity',
#    description='This is a test opportunity for testing purposes.',
#    start_date=datetime.utcnow(),
#    end_date=datetime.utcnow() + timedelta(days=7)
# )

# # Create a new registration
# registration1 = Registration(
#    account_id=account1.id,
#    opportunity_id=opportunity1.id
# )


if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # delete current data
        print("clearing database")
        Account.query.delete()
        Opportunity.query.delete()
        Registration.query.delete()
        print("database cleared")
        # create the database if not created
        db.create_all()
        # Seed code goes here!
        print("seeding accounts...")
        acc = create_accounts()
        db.session.add_all(acc)
        
        print("finished seeding accounts")

        print("seeding events...")
        opp = create_opportunities()
        db.session.add_all(opp)
        
        print("finished seeding events")

        print("seeding registrations...")

        reg = create_registration()
        db.session.add_all(reg)
        print("finished seeding registrations")
        db.session.commit()
        print("finished seeding!!")


    # db.session.add(account1)
    # db.session.add(opportunity1)
    # db.session.add(registration1)

    #    # Commit the session to save the changes to the database
    # db.session.commit()