from app.RegaliApp.Person.Infrastructure.Entities.AlchemyPerson import AlchemyPerson
from app import db

class AlchemyPersonRepository:
    @staticmethod
    def findOneByGoogleId(google_id):
        person = db.session.query(AlchemyPerson).filter(AlchemyPerson.google_id == google_id).first()

        return person

    @staticmethod
    def findOneByUserId(user_id):
        person = db.session.query(AlchemyPerson).filter(AlchemyPerson.id == user_id).first()

        return person

    @staticmethod
    def findOneByEmail(email):
        person = db.session.query(AlchemyPerson).filter(AlchemyPerson.email == email).first()

        return person

    @staticmethod
    def save(AlchemyPerson):
        db.session.add(AlchemyPerson)
        db.session.commit()
    