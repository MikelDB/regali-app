import sys
from app.RegaliApp.List.Infrastructure.Entities.AlchemyGiftList import AlchemyGiftList
from app.RegaliApp.List.Domain.Repositories.GiftListRepository import GiftListRepository
from app import db

class AlchemyGiftListRepository(GiftListRepository):
    def findOneByReference(self, reference):
        print(reference, file=sys.stdout)
        gift_list = db.session.query(AlchemyGiftList).filter(AlchemyGiftList.reference == reference).first()

        return gift_list

    @staticmethod
    def save(AlchemyGiftList):
        db.session.add(AlchemyGiftList)
        db.session.commit()

    @staticmethod
    def deleteListByReference(reference):
        gift_list = db.session.query(AlchemyGiftList).filter(AlchemyGiftList.reference == reference).first()

        db.session.delete(gift_list)
        db.session.commit()
    