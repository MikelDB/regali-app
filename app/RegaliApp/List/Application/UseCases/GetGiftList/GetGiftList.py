from injector import inject
from app.RegaliApp.List.Domain.Services.GetGiftListByReferenceService import GetGiftListByReferenceService

class GetGiftListUseCase:
    @inject
    def __init__(self, get_gift_list_by_reference: GetGiftListByReferenceService):
        self.get_gift_list_by_reference = get_gift_list_by_reference

    def execute(self, reference):
        return self.get_gift_list_by_reference.execute(reference)