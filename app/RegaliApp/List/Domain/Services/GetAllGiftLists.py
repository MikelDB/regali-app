from injector import inject
from app.RegaliApp.List.Domain.Repositories.GiftListRepository import GiftListRepository


class GetAllGiftLists:
    @inject
    def __init__(self, gift_list_repository: GiftListRepository):
        self.gift_list_repository = gift_list_repository


    def execute(self):
        return self.gift_list_repository.findAll()