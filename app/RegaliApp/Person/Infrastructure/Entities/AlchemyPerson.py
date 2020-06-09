from app.RegaliApp.Person.Domain.Entities.Person import Person
from app import db
from sqlalchemy.orm import mapper

metadata = db.MetaData()

alchemy_person = db.Table(
    'person', 
    metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('google_id', db.String(50)),
    db.Column('name', db.String(64)),
    db.Column('email', db.String(32)),
    db.Column('is_active', db.Boolean),
    db.Column('is_authenticated', db.Boolean),
    db.Column('profile_pic', db.Text),
)


class AlchemyPerson(Person):
    pass


mapper(AlchemyPerson, alchemy_person)
