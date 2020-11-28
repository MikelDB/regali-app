import uuid

from app.RegaliApp.List.Domain.Factories.GiftListElementFactory import GiftListElementFactory
from app.RegaliApp.List.Infrastructure.Entities.AlchemyGiftList import AlchemyGiftListElement

class AlchemyGiftListElementFactory(GiftListElementFactory):
    def build_gift_list_element_from_parameters(self, list_id: int, url: str) -> AlchemyGiftListElement:
        return AlchemyGiftListElement(
            None,
            str(uuid.uuid4()),
            list_id,
            'Hola',
            url,
            None,
            None,
        )
