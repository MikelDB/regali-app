# pylint: disable=E1101
from app.regali_app.list.infrastructure.entities.alchemy_gift_list import AlchemyGiftList
from app.regali_app.list.domain.repositories.gift_list_repository import GiftListRepository
from app import db

class AlchemyGiftListRepository(GiftListRepository):
    def find_one_by_reference(self, reference):
        gift_list = db.session.query(AlchemyGiftList).filter(AlchemyGiftList.reference == reference).first()

        return gift_list

    def save(self, gift_list: AlchemyGiftList):
        db.session.add(gift_list)
        db.session.commit()
        return gift_list

    def delete_list_by_reference(self, reference):
        gift_list = db.session.query(AlchemyGiftList).filter(AlchemyGiftList.reference == reference).first()

        db.session.delete(gift_list)
        db.session.commit()

    def find_all(self):
        return db.session.query(AlchemyGiftList).all()
