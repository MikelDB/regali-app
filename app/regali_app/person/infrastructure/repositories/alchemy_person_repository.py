# pylint: disable=E1101
from app.regali_app.person.infrastructure.entities.alchemy_person import AlchemyPerson
from app.regali_app.person.domain.repositories.person_repository import PersonRepository
from app import db

class AlchemyPersonRepository(PersonRepository):
    @staticmethod
    def find_one_by_google_id(google_id):
        person = db.session.query(AlchemyPerson).filter(AlchemyPerson.google_id == google_id).first()

        return person

    @staticmethod
    def find_one_by_user_id(user_id):
        person = db.session.query(AlchemyPerson).filter(AlchemyPerson.id == user_id).first()

        return person

    @staticmethod
    def find_one_by_email(email):
        person = db.session.query(AlchemyPerson).filter(AlchemyPerson.email == email).first()

        return person

    @staticmethod
    def save(person):
        db.session.add(person)
        db.session.commit()

    @staticmethod
    def find_one_by_public_id(public_id):
        person = db.session.query(AlchemyPerson).filter(AlchemyPerson.public_id == public_id).first()

        return person
