import uuid

from app.RegaliApp.List.Domain.Factories.GiftListFactory import GiftListFactory
from app.RegaliApp.List.Infrastructure.Entities.AlchemyGiftList import AlchemyGiftList

class AlchemyGiftListFactory(GiftListFactory):
    def build_gift_list_from_parameters(self, user_id: int, name: str):
        return AlchemyGiftList(
            None,
            str(uuid.uuid4()),
            user_id,
            name,
            True,       
            True,
            None,
            None
        )