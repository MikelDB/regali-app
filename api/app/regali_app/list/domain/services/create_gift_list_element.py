from injector import inject
from app.regali_app.list.domain.repositories.gift_list_element_repository import GiftListElementRepository
from app.regali_app.list.domain.entities.gift_list_element import GiftListElement


class CreateGiftListElement:
    @inject
    def __init__(self, gift_list_element_repository: GiftListElementRepository):
        self.gift_list_element_repository = gift_list_element_repository


    def execute(self, gift_list_element) -> GiftListElement:
        return self.gift_list_element_repository.save(gift_list_element)
