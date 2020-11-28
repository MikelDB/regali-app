from injector import inject
from app.RegaliApp.List.Domain.Repositories.GiftListElementRepository import GiftListElementRepository
from app.RegaliApp.List.Domain.Entities.GiftListElement import GiftListElement


class CreateGiftListElement:
    @inject
    def __init__(self, gift_list_element_repository: GiftListElementRepository):
        self.gift_list_element_repository = gift_list_element_repository


    def execute(self, gift_list_element) -> GiftListElement:
        return self.gift_list_element_repository.save(gift_list_element)