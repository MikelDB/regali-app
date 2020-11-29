import uuid

from app.regali_app.list.domain.factories.gift_list_element_factory import GiftListElementFactory
from app.regali_app.list.infrastructure.entities.alchemy_gift_list import AlchemyGiftListElement

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
