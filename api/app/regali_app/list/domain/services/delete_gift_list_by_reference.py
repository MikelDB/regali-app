from injector import inject
from app.regali_app.list.domain.repositories.gift_list_repository import GiftListRepository


class DeleteGiftListByReference:
    @inject
    def __init__(self, gift_list_repository: GiftListRepository):
        self.gift_list_repository = gift_list_repository


    def execute(self, reference):
        return self.gift_list_repository.delete_list_by_reference(reference)
