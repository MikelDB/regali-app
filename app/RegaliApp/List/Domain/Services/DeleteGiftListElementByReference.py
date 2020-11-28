from injector import inject
from app.RegaliApp.List.Domain.Repositories.GiftListElementRepository import GiftListElementRepository


class DeleteGiftListElementByReference:
    @inject
    def __init__(self, gift_list_element_repository: GiftListElementRepository):
        self.gift_list_element_repository = gift_list_element_repository


    def execute(self, reference):
        return self.gift_list_element_repository.deleteListByReference(reference)