from injector import inject
from app.RegaliApp.List.Domain.Repositories.GiftListRepository import GiftListRepository
from app.RegaliApp.List.Domain.Entities.GiftList import GiftList


class CreateGiftList:
    @inject
    def __init__(self, gift_list_repository: GiftListRepository):
        self.gift_list_repository = gift_list_repository


    def execute(self, gift_list) -> GiftList:
        return self.gift_list_repository.save(gift_list)