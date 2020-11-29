import uuid

from app.regali_app.list.domain.factories.gift_list_factory import GiftListFactory
from app.regali_app.list.infrastructure.entities.alchemy_gift_list import AlchemyGiftList, AlchemyGiftListElement

class AlchemyGiftListFactory(GiftListFactory):
    def build_gift_list_from_parameters(self, user_id: int, name: str, list_elements: dict):
        alchemy_gift_list = AlchemyGiftList(
            None,
            str(uuid.uuid4()),
            user_id,
            name,
            True,
            True,
            None,
            None
        )

        alchemy_gift_list.elements = self.build_gift_list_elements_from_parameters(list_elements)

        return alchemy_gift_list

    @staticmethod
    def build_gift_list_elements_from_parameters(list_elements: dict) -> list:
        gift_list_elements = []

        for list_element in list_elements:
            gift_list_elements.append(
                AlchemyGiftListElement(
                    list_element['id'],
                    str(uuid.uuid4()),
                    None,
                    list_element['name'],
                    list_element['url'],
                    None,
                    None
                )
            )

        return gift_list_elements
