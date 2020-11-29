from injector import inject
from app.regali_app.list.domain.repositories.gift_list_repository import GiftListRepository
from app.regali_app.list.domain.entities.gift_list import GiftList


class CreateGiftList:
    @inject
    def __init__(self, gift_list_repository: GiftListRepository):
        self.gift_list_repository = gift_list_repository


    def execute(self, gift_list) -> GiftList:
        return self.gift_list_repository.save(gift_list)
