import sys
from app.RegaliApp.List.Infrastructure.Entities.AlchemyGiftList import AlchemyGiftList
from app.RegaliApp.List.Domain.Repositories.GiftListRepository import GiftListRepository
from app import db

class AlchemyGiftListRepository(GiftListRepository):
    def findOneByReference(self, reference):
        gift_list = db.session.query(AlchemyGiftList).filter(AlchemyGiftList.reference == reference).first()

        return gift_list

    def save(self, AlchemyGiftList):
        db.session.add(AlchemyGiftList)
        db.session.commit()
        return AlchemyGiftList

    def deleteListByReference(self, reference):
        gift_list = db.session.query(AlchemyGiftList).filter(AlchemyGiftList.reference == reference).first()

        db.session.delete(gift_list)
        db.session.commit()
    
    def findAll(self):
        return db.session.query(AlchemyGiftList).all()
