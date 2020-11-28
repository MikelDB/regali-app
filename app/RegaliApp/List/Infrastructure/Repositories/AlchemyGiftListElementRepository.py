import sys
from app.RegaliApp.List.Infrastructure.Entities.AlchemyGiftList import AlchemyGiftListElement
from app.RegaliApp.List.Domain.Repositories.GiftListElementRepository import GiftListElementRepository
from app import db

class AlchemyGiftListElementRepository(GiftListElementRepository):
    def save(self, AlchemyGiftListElement):
        db.session.add(AlchemyGiftListElement)
        db.session.commit()
        return AlchemyGiftListElement

    def deleteListByReference(self, reference):
        gift_list_element = db.session.query(AlchemyGiftListElement).filter(AlchemyGiftListElement.reference == reference).first()

        db.session.delete(gift_list_element)
        db.session.commit()
