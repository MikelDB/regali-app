from . import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(36), index=False, unique=True)
    email = db.Column(db.String(36), index=False, unique=True)
    name = db.Column(db.String(16), index=False, unique=False)
    is_active = db.Column(db.Boolean, index=False, unique=False)
    is_authenticated = db.Column(db.Boolean, index=False, unique=False, default=True)
    profile_pic = db.Column(db.Text, index=False, unique=False)

    events = db.relationship('Event', backref='person', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return '<Person {}>'.format(self.id)

    def get_id(self):
        return self.id

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=False, unique=False)
    reference = db.Column(db.String(36), index=False, unique=True)
    created_at = db.Column(db.Date, index=False, unique=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __repr__(self):
        return '<Event {}>'.format(self.id)
