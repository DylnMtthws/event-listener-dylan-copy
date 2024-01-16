#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Account, Registration, Opportunity 

class Opportunities(Resource):
    def get(self):
        opportunities = [opportunity.to_dict() for opportunity in Opportunity.query.all()]
        return opportunities, 200
    
    def post(self):
        data = request.get_json()
        try:
            new_opportunity = Opportunity(
                title = data['title'],
                description = data["description"],
                start_date = data["start_date"],
                end_date = data["end_date"]
            )
            db.session.add(new_opportunity)
            db.session.commit()
            return new_opportunity.to_dict(only = ("title", "description", "start_date", "end_date")), 200
        except ValueError:
            return{
                "errors": ["validation errors"]
                }, 400

api.add_resource(Opportunities, "/events")

class OpportunityById(Resource):
        def get(self, id):
            opportunities = Opportunity.query.filter_by(id=id).first()
            return opportunities.to_dict(only=("title", "description", "start_date", "end_date")), 200

        def patch(self, id):
            opportunity = Opportunity.query.filter_by(id=id).first()
            if not opportunity:
                return {
                "error": "Event not found"
                }, 404
            data = request.get_json()

            try:
                for key in data:
                    setattr(opportunity, key, data[key])
                db.session.add(opportunity)
                db.session.commit()
            except ValueError as e:
                print(e.__str__())
                return {
                "error": "validation errors"
                }, 400

            return opportunity.to_dict(only=("title", "description", "start_date", "end_date")), 200                

        def delete(self, id):
            opportunity = Opportunity.query.filter_by(id=id).first()
            if not opportunity:
                return {"error": "Event not found"}, 404
            
            db.session.delete(opportunity)
            db.session.commit()
            return "", 204

api.add_resource(OpportunityById, "/events/<int:id>")

class Accounts(Resource):
    def get(self):
        accounts = [account.to_dict() for account in Account.query.all()]
        return accounts, 200
    
    def post(self):
        data = request.get_json()
        try:
            new_account = Account(
                username = data["username"],
                password_hash = data["password"],
                name = data["name"],
                email = data["email"],
                role = data["role"]
            )
            db.session.add(new_account)
            db.session.commit()
            return new_account.to_dict(only=("name", "role", "username", "email")), 201
        except Exception as e:
            print(e.__str__())
            return {
                "errors": ["validation errors"]
            }, 400
        

api.add_resource(Accounts, "/volunteers")

class AccountById(Resource):
    def get(self, id):
        account = Account.query.filter_by(id=id).first()
        return account.to_dict(), 200
    
    def patch(self, id):
        account = Account.query.filter_by(id=id).first()
        if not account:
            return {
            "error": "Event not found"
            }, 404
        data = request.get_json()

        try:
            for key in data:
                setattr(account, key, data[key])
            db.session.add(account)
            db.session.commit()
        except ValueError as e:
            print(e.__str__())
            return {
            "error": "validation errors"
            }, 400

        return account.to_dict(only=("id","name", "role", "username", "email")), 200 
    
    def delete(self, id):
        account = Account.query.filter_by(id=id).first()
        if not account:
            return {
                "error": "Event not found"
                }, 404
        db.session.delete(account)
        db.session.commit()
        return "", 204
    
api.add_resource(AccountById, "/volunteers/<int:id>")


class Registrations(Resource):
    def get(self):
        registrations = [registration.to_dict() for registration in Registration.query.all()]
        return registrations, 200
    
    def post(self):
        data = request.get_json()
        try:
            new_registration= Registration(
                # registration_date = data["registration_date"],
                account_id = data["account_id"],
                opportunity_id = data["opportunity_id"]
            )
            db.session.add(new_registration)
            db.session.commit()
            return new_registration.to_dict(only=("registration_date", "account_id", "opportunity_id")), 201
        except ValueError as e:
            print (e.__str__())
            return {
                "errors": ["validation errors"]
            }, 400

api.add_resource(Registrations, "/registrations")

class RegistrationById(Resource):

    def get(self, id):
        registration = Registration.query.filter_by(id=id).first()
        return registration.to_dict(only=("registration_date", "account_id", "opportunity_id")), 200

    def delete(self, id):
        registration = Registration.query.filter_by(id=id).first()
        if not registration:
            return {"error": "Event not found"}, 404
        
        db.session.delete(registration)
        db.session.commit()
        return "", 204
    
    def patch(self, id):
        registration = Registration.query.filter_by(id=id).first()
        if not registration:
            return {
            "error": "Event not found"
            }, 404
        data = request.get_json()

        try:
            for key in data:
                setattr(registration, key, data[key])
            db.session.add(registration)
            db.session.commit()
        except ValueError as e:
            print(e.__str__())
            return {
            "error": "validation errors"
            }, 400

        return registration.to_dict(only=("registration_date", "account_id", "opportunity_id")), 200 

api.add_resource(RegistrationById, "/registrations/<int:id>")

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = Account.query.filter(username == username).first()
        if user:
            if user.authenticate(password):
                session['user_id'] = user.id
                return user.to_dict(), 200
        return {
            'error': 'Unauthorized'
            }, 401
    
api.add_resource(Login, '/login')
    
# check session 
class CheckSession(Resource):
    def get(self):
        user = Account.query.filter(Account.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {
                'message': '401: Not Authorized'
                }, 401

api.add_resource(CheckSession, '/check_session')

# logout
class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {'message':'204: No Content'}
    
api.add_resource(Logout, '/logout')


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

