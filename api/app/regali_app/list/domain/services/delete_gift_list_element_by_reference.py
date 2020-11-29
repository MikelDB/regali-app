from injector import inject
from app.regali_app.list.domain.repositories.gift_list_element_repository import GiftListElementRepository


class DeleteGiftListElementByReference:
    @inject
    def __init__(self, gift_list_element_repository: GiftListElementRepository):
        self.gift_list_element_repository = gift_list_element_repository


    def execute(self, reference):
        return self.gift_list_element_repository.delete_list_by_reference(reference)
