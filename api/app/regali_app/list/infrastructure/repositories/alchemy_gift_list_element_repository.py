# pylint: disable=E1101
from app.regali_app.list.infrastructure.entities.alchemy_gift_list import AlchemyGiftListElement
from app.regali_app.list.domain.repositories.gift_list_element_repository import GiftListElementRepository
from app import db

class AlchemyGiftListElementRepository(GiftListElementRepository):
    def save(self, gift_list_element: AlchemyGiftListElement) -> AlchemyGiftListElement:
        db.session.add(gift_list_element)
        db.session.commit()
        return gift_list_element

    def delete_list_by_reference(self, reference):
        gift_list_element = db.session.query(
            AlchemyGiftListElement
        ).filter(AlchemyGiftListElement.reference == reference).first()

        db.session.delete(gift_list_element)
        db.session.commit()
