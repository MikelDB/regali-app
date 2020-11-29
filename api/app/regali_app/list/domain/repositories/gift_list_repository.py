from app.regali_app.list.domain.entities.gift_list import GiftList

class GiftListRepository:
    def find_one_by_reference(self, reference) -> GiftList:
        pass

    def save(self, gift_list: GiftList) -> GiftList:
        pass

    def delete_list_by_reference(self, reference):
        pass

    def find_all(self):
        pass
