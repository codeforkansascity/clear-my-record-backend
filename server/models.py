from clear_my_record_backend.server import dbs
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum
from datetime import datetime

charge_types = Enum('CHARGE', 'FELONY MISDEMEANOR')
class_types = Enum('CLASS', 'A B C D E UNDEFINED')
user_types = Enum('USER', 'CLINIC_STAFF LAWYER CLIENT ADMIN SUPER_ADMIN')

class Qualifying_Question(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    question = dbs.Column(dbs.Text)
    help_text = dbs.Column(dbs.Text)
    disqualifying_answer = dbs.Column(dbs.String(250))


class Qualifying_Answer(dbs.Model):
    # First Integer ID is set as autoincrement in SQLAlchemy
    id = dbs.Column(dbs.Integer, primary_key=True)
    user_session = dbs.Column(dbs.String(250), index=True, unique=False)
    question_id = dbs.Column(dbs.String(250))
    answer = dbs.Column(dbs.Text)
    qualifying_answer = dbs.Column(dbs.String(250))
    question_version_number = dbs.Column(dbs.Float(asdecimal=True))
    timestamp = dbs.Column(dbs.DateTime, index=True)
    answerer_id = dbs.Column(dbs.Integer, dbs.ForeignKey("user.id"))

    def __init__(self, *data, **kwargs):
        super(Qualifying_Answer, self).__init__(**kwargs)
        for dictionary in data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])


class User(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    username = dbs.Column(dbs.String(32), index=True, unique=True)
    email = dbs.Column(dbs.String(120), index=True, unique=True)
    pw_hash = dbs.Column(dbs.String(128))
    submissions = dbs.relationship(
        "Qualifying_Answer", backref="author", lazy="dynamic")
<<<<<<< HEAD
    user_type = dbs.Column(dbs.Enum(user_types))
=======
    user_type = dbs.Column(dbs.String)
>>>>>>> more server/posts work
    clients = dbs.relationship('Client', backref='user', lazy='dynamic')
    created_at = dbs.Column(dbs.DateTime, default=datetime.utcnow)
    updated_at = dbs.Column(dbs.DateTime, default=datetime.utcnow)

    def __init__(self, *data, **kwargs):
        super(User, self).__init__(**kwargs)
        for dictionary in data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def update(self, *data, **kwargs):
        for dictionary in data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
        return self


    def __repr__(self):
        return "<USER: {}>".format(self.username)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def exists(self):
        name = User.query.filter_by(username=self.username).first()
        email = User.query.filter_by(email=self.email).first()
        return name is not None or email is not None

    @dbs.validates('user_type')
    def validate_user_type(self, key, user_type):
        assert str(user_type).replace(' ', '_').upper() in user_types.__members__
        return user_type

    @classmethod
    def find_by_email(cls, _email):
        return cls.query.filter_by(email=_email).first()

    @classmethod
    def find_by_username(cls, _username):
        return cls.query.filter_by(username=_username).first()

class Client(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    user_id = dbs.Column(dbs.Integer, dbs.ForeignKey('user.id'))
    full_name = dbs.Column(dbs.String)
    # 123-456-7890
    phone = dbs.Column(dbs.VARCHAR(12))
    email = dbs.Column(dbs.String)
    sex = dbs.Column(dbs.String)
    race = dbs.Column(dbs.String)
    dob = dbs.Column(dbs.Date)
    address_line_1 = dbs.Column(dbs.String)
    address_line_2 = dbs.Column(dbs.String)
    city = dbs.Column(dbs.String)
    state = dbs.Column(dbs.String)
    # 64111 or 64111-0000
    zip_code = dbs.Column(dbs.VARCHAR(10))
    license_number = dbs.Column(dbs.String)
    license_issuing_state = dbs.Column(dbs.VARCHAR(2))
    license_expiration_date = dbs.Column(dbs.Date)
    status = dbs.Column(dbs.String)
    active = dbs.Column(dbs.Boolean)
    convictions = dbs.relationship('Conviction', backref='client', lazy='dynamic')
    created_at = dbs.Column(dbs.DateTime, default=datetime.utcnow)
    updated_at = dbs.Column(dbs.DateTime, default=datetime.utcnow)
<<<<<<< HEAD
=======
    notes = dbs.Column(dbs.String)
>>>>>>> more server/posts work

    def __init__(self, *data, **kwargs):
        super(Client, self).__init__(**kwargs)
        for dictionary in data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

class Conviction(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    client_id = dbs.Column(dbs.Integer, dbs.ForeignKey('client.id'))
    case_number = dbs.Column(dbs.String)
    agency = dbs.Column(dbs.String)
    court_name = dbs.Column(dbs.String)
    court_city_county = dbs.Column(dbs.String)
    judge = dbs.Column(dbs.String)
    record_name = dbs.Column(dbs.String)
    release_status = dbs.Column(dbs.String)
    release_date = dbs.Column(dbs.Date)
    charges = dbs.relationship('Charge', backref='conviction', lazy='dynamic')
    created_at = dbs.Column(dbs.DateTime, default=datetime.utcnow)
    updated_at = dbs.Column(dbs.DateTime, default=datetime.utcnow)
<<<<<<< HEAD
=======
    notes = dbs.Column(dbs.String)
>>>>>>> more server/posts work

    def __init__(self, *data, **kwargs):
        super(Conviction, self).__init__(**kwargs)
        for dictionary in data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])


class Charge(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    conviction_id = dbs.Column(dbs.Integer, dbs.ForeignKey('conviction.id'))
    charge = dbs.Column(dbs.String)
    citation = dbs.Column(dbs.String)
    sentence = dbs.Column(dbs.String)
    class_type = dbs.Column(dbs.String)
    charge_type = dbs.Column(dbs.String)
    eligible = dbs.Column(dbs.Boolean)
    please_expunge = dbs.Column(dbs.Boolean)
    created_at = dbs.Column(dbs.DateTime, default=datetime.utcnow)
    updated_at = dbs.Column(dbs.DateTime, default=datetime.utcnow)
    notes = dbs.Column(dbs.String)

    def __init__(self, *data, **kwargs):
        super(Charge, self).__init__(**kwargs)
        for dictionary in data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @dbs.validates('class_type')
    def validate_class_type(self, key, class_type):
        assert str(class_type).replace(' ', '_').upper() in class_types.__members__
        return class_type

    @dbs.validates('charge_type')
    def validate_charge_type(self, key, charge_type):
        assert str(charge_type).replace(' ', '_').upper() in charge_types.__members__
        return charge_type
