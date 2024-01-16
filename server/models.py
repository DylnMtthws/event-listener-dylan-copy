from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from datetime import datetime
from config import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class Account(db.Model, SerializerMixin):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    email = db.Column(db.String)
    role = db.Column(db.String)

    registrations = db.relationship('Registration', back_populates= 'account')
    serialize_rules = ('-registrations.account',)

    @validates('name')
    def validate_name(self,key,name):
        if not name:
            raise ValueError('must be a name')
        return name

    @validates('role')
    def validate_role(self,key,role):
        r = ["Admin", "Volunteer"]
        if role not in r:
            raise ValueError('must be Admin or Volunteer')
        return role

    def __repr__(self):
        return f'<Account {self.id}: {self.name}>'
    
    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        # utf-8 encoding and decoding is required in python 3
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))


class Opportunity(db.Model, SerializerMixin):
    __tablename__= 'opportunities'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)

    registrations = db.relationship('Registration', back_populates = 'opportunity')

    serialize_rules = ('-registrations.opportunity',)

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 5:
            raise ValueError('description must be present and at least 5 characters long ')
        return description 

    def __repr__(self):
        return f'<Opportunity {self.id}: {self.title}>'

class Registration(db.Model, SerializerMixin):
    __tablename__ = 'registrations'
    id = db.Column(db.Integer, primary_key = True)
    registration_date = db.Column(db.String, nullable=False, default=datetime.utcnow)

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable = False)
    opportunity_id = db.Column(db.Integer, db.ForeignKey('opportunities.id'), nullable = False)

    account = db.relationship('Account', back_populates = 'registrations')
    opportunity = db.relationship('Opportunity', back_populates = 'registrations')

    serialize_rules = ('-account.registrations', '-opportunity.registrations',)

    def __repr__(self):
        return f'<Registration {self.id}>'





