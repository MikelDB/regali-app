from injector import inject
from app.regali_app.list.domain.repositories.gift_list_repository import GiftListRepository


class GetAllGiftLists:
    @inject
    def __init__(self, gift_list_repository: GiftListRepository):
        self.gift_list_repository = gift_list_repository


    def execute(self):
        return self.gift_list_repository.find_all()
